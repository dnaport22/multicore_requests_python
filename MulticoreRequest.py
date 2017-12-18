#!usr/bin/python3.5.0
# -*- coding: utf8 -*-e
from multiprocessing import Pool
import requests as req

class MulticoreRequest():
    """
    MulticoreRequest module wraps up multiprocessing
    and requests module together to speed up rest calls made in bulk.
    """

    """
    call_pack | dict
        {
            'url': 'http://...',
            'type': 'get|post',
            'data': 'stringified json object'
        }
    """
    call_pack = None

    def __init__(self, call_pack, procs=10):
        self.__set_call_pack(call_pack)
        self.procs = procs

    def make_call(self):
        """
        :return object:
        """
        self._run_multicore(
            self.call,
            MulticoreRequest.call_pack
        )

    def _run_multicore(self, worker, programs):
        """
        :param worker:
        :param programms:
        :return object:
        """
        p = Pool(self.procs)
        p.map(worker, programs)

    @staticmethod
    def call(data):
        """
        :param data:
        :return object:
        """
        if data['type'] == 'get':
            return req.get(data['url'])

        if data['type'] == 'post':
            return req.post(
                data['url'],
                data['data']
            )

    def __set_call_pack(self, call_pack):
        """
        :param call_pack:
        :raise exception:
        :return mixed:
        """
        if type(call_pack).__name__ == 'list':
            self.procs = 50
            self._run_multicore(
                MulticoreRequest.check_required_keys,
                call_pack
            )
        elif True:
            raise Exception('list type required')

        MulticoreRequest.call_pack = call_pack

    def get_data_pack(self):
        """
        :return dict:
        """
        return MulticoreRequest.call_pack

    @staticmethod
    def check_required_keys(data):
        """
        :param data:
        :return mixed:
        """
        try:
            assert data['url'], "URL required"
            assert data['type'], "TYPE required"
        except (KeyError, AssertionError) as e:
            raise Exception("{} required".format(e))

        return True