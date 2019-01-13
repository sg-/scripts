# https://os.mbed.com/users/sam_grove/notebook/seeeduino-arch-pro-notes/
#   Data recorded in the wikipage but it seems that using pyocd for flashing will increase the testing time
#   by 2.5x. This does not account looking deeper into pyocd and determining if there are more improvements
#   rather treats it like a black box

def find(key, dictionary):
    for k, v in dictionary.iteritems():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result

def main():
    import json, time
    from pyOCD.board import MbedBoard
    file = "/Users/samgro01/mbed-workspace/mbed-os/BUILD/tests/ARCH_PRO/GCC_ARM/test_spec.json"
    f = open(file, "r") 
    dictionary = json.loads(f.read())
    data = list(find("path", dictionary))
    # Here we should do some sort of delta sort algorithm where we order the tests based on difference in binary
    #   files such that a fast_program (crc check) programmer would spend a little time as possible programming
    #   the devices. If using pyocd for programming, its estimated that about 2/3 of total testing time is spent
    #   writting to flash and verifying and there doesnt seem to be much difference in the pyocd programming methods.
    #   We should also look at verify as part of the flash algo program page operation. Not sure how pyocd does verify
    #   and if that was a second step after programming, moving into the program operation could be an optimization
    #   (read and compare with buffer)
    for d in data:
        with MbedBoard.chooseBoard(board_id="9004") as board:        
            board.flash.flashBinary(d, fast_verify=true, smart_flash=False, chip_erase=True)
            board.target.reset()
            # uninit seems to do a reset and run but need to double check that and if not then board.target.resume()
            #   or similar will be necessary
            board.uninit()
            # Here we are executing a test. The 66 test cases I looked at spent 147 seconds exeucting tests so mocking
            #   that by dividing by 66 which is a little less than 3 seconds per test
            time.sleep(3)
            print d
            # this does not account for any 9600 baud rate data that the test harness and runner uses. Assumption is that
            #   the serial data time is already accounted for in the test execution time as measured by greentea


if __name__ == "__main__":
    main()
