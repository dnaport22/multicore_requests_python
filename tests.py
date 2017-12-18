import unittest
import time
from MulticoreRequest import MulticoreRequest

class TestMulticoreProcess(unittest.TestCase):

    def test_complete_key_checking(self):
        complete_set = {
            'url': 'http://google.com',
            'type': 'get'
        }

        self.assertTrue(
            MulticoreRequest.check_required_keys(complete_set)
        )

    def test_check_for_missing_keys(self):
        missing_url_set = {
            'type': 'get'
        }

        missing_type_set = {
            'url': 'http://google.com'
        }

        with self.assertRaises(Exception) as ex:
            MulticoreRequest.check_required_keys(missing_url_set)
            MulticoreRequest.check_required_keys(missing_type_set)

    def test_request_performance(self):
        data = [{'url': 'https://httpbin.org/get', 'type': 'get'}]
        sample = 30
        for i in range(sample - 1):
            data.append(data[0])

        mc_req = MulticoreRequest(data)
        time_started = time.time()
        mc_req.make_call()
        time_finished = time.time()
        time_elapsed = time_finished - time_started
        print('Time elapsed = {}'.format(time_elapsed))


if __name__ == '__main__':
    unittest.main()