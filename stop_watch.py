import time
import argparse
import sys
        

def get_parser():
  parser = argparse.ArgumentParser(description='set a countdown time limit')
  parser.add_argument('-limit', metavar='limit', type=int, help='provide limit', required=True)
  return parser


def main():

  parser = get_parser()
  args = vars(parser.parse_args())
  time_limit = args['limit'] * 60 # Converting to mins

  secs = 0
  """
    CURSOR_UP_ONE, ERASE_LINE helps to delete the last printed line
  """
  CURSOR_UP_ONE = '\x1b[1A'
  ERASE_LINE = '\x1b[2K'
  start_time = time.time()
  is_interupted = False
  print('Start time: {}'.format(time.ctime()))
  while secs != time_limit:
      try:
          print ("Timer: {}".format(mins))
          sys.stdout.write(CURSOR_UP_ONE)
          sys.stdout.write(ERASE_LINE)
          time.sleep(1)
          # Increment the secs
          secs += 1
      except KeyboardInterrupt:
          is_interupted = True
          break
  print_result(start_time)

def print_result(start_time):
  print('Stop time: {}'.format(time.ctime()))
  endtime = time.time()
  print('Total Time:', round(endtime - start_time),'secs')

if __name__ == '__main__':
    main()