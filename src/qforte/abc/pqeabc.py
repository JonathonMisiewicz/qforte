from abc import abstractmethod
from qforte.abc.algorithm import Algorithm

class PQE(Algorithm):

    @abstractmethod
    def build_Uvqc(self):
        pass

    @abstractmethod
    def measure_energy(self):
        pass

    @abstractmethod
    def energy_feval(self):
        pass

    @abstractmethod
    def solve(self):
        pass

    def verify_required_PQE_attributes(self):
        # if self._optimizer is None:
        #     raise NotImplementedError('Concrete PQE class must define self._optimizer attribute.')

        if self._converged is None:
            raise NotImplementedError('Concrete PQE class must define self._converged attribute.')

        # if self._final_result is None:
        #     raise NotImplementedError('Concrete PQE class must define self._final_result attribute.')

        if self._opt_maxiter is None:
            raise NotImplementedError('Concrete PQE class must define self._opt_maxiter attribute.')

        if self._opt_thresh is None:
            raise NotImplementedError('Concrete PQE class must define self._opt_thresh attribute.')
