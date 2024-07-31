class Codigo:
    def __init__(self,local,num_codigo):
        self._local = local
        self._num_codigo = num_codigo

    def __str__(self):
        return f'{self._local}, {self._num_codigo}'
