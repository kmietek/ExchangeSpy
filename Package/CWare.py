class CWare:
    def __getName__(self):
        raise NotImplementedError

    def __setName__(self, parameter_list):
        raise NotImplementedError

    def __setPrice__(self, parameter_list):
        raise NotImplementedError

    def __getPrice__(self, parameter_list):
        raise NotImplementedError
