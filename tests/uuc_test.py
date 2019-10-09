import unittest
from qforte import qforte
from qforte import vqe

class UccTests(unittest.TestCase):
    def test_He_uccsd_exact(self):
        print('\n')
        # The FCI energy for He in a cc-pvdz basis
        E_fci = -2.8875948310909374

        # The He hamilitonian
        circ_vec = [qforte.QuantumCircuit(),
        qforte.build_circuit('Z_0'),
        qforte.build_circuit('Y_0 Z_1 Y_2'),
        qforte.build_circuit('X_0 Z_1 X_2'),
        qforte.build_circuit('Z_1'),
        qforte.build_circuit('Y_1 Z_2 Y_3'),
        qforte.build_circuit('X_1 Z_2 X_3'),
        qforte.build_circuit('Z_2'),
        qforte.build_circuit('Z_3'),
        qforte.build_circuit('Z_4'),
        qforte.build_circuit('Z_5'),
        qforte.build_circuit('Z_6'),
        qforte.build_circuit('Z_7'),
        qforte.build_circuit('Z_8'),
        qforte.build_circuit('Z_9'),
        qforte.build_circuit('Z_0 Z_1'),
        qforte.build_circuit('Y_0 Y_2'),
        qforte.build_circuit('X_0 X_2'),
        qforte.build_circuit('Z_0 Y_1 Z_2 Y_3'),
        qforte.build_circuit('Z_0 X_1 Z_2 X_3'),
        qforte.build_circuit('Y_0 X_1 X_2 Y_3'),
        qforte.build_circuit('X_0 X_1 Y_2 Y_3'),
        qforte.build_circuit('Y_0 Y_1 X_2 X_3'),
        qforte.build_circuit('X_0 Y_1 Y_2 X_3'),
        qforte.build_circuit('Y_0 X_1 X_4 Y_5'),
        qforte.build_circuit('X_0 X_1 Y_4 Y_5'),
        qforte.build_circuit('Y_0 Y_1 X_4 X_5'),
        qforte.build_circuit('X_0 Y_1 Y_4 X_5'),
        qforte.build_circuit('Y_0 X_1 X_6 Y_7'),
        qforte.build_circuit('X_0 X_1 Y_6 Y_7'),
        qforte.build_circuit('Y_0 Y_1 X_6 X_7'),
        qforte.build_circuit('X_0 Y_1 Y_6 X_7'),
        qforte.build_circuit('Y_0 X_1 X_8 Y_9'),
        qforte.build_circuit('X_0 X_1 Y_8 Y_9'),
        qforte.build_circuit('Y_0 Y_1 X_8 X_9'),
        qforte.build_circuit('X_0 Y_1 Y_8 X_9'),
        qforte.build_circuit('Z_0 Z_2'),
        qforte.build_circuit('Z_0 Z_3'),
        qforte.build_circuit('Y_0 Z_1 Y_2 Z_3'),
        qforte.build_circuit('X_0 Z_1 X_2 Z_3'),
        qforte.build_circuit('Y_0 Z_1 Z_2 X_3 X_4 Y_5'),
        qforte.build_circuit('X_0 Z_1 Z_2 X_3 Y_4 Y_5'),
        qforte.build_circuit('Y_0 Z_1 Z_2 Y_3 X_4 X_5'),
        qforte.build_circuit('X_0 Z_1 Z_2 Y_3 Y_4 X_5'),
        qforte.build_circuit('Y_0 Z_1 Z_2 X_3 X_6 Y_7'),
        qforte.build_circuit('X_0 Z_1 Z_2 X_3 Y_6 Y_7'),
        qforte.build_circuit('Y_0 Z_1 Z_2 Y_3 X_6 X_7'),
        qforte.build_circuit('X_0 Z_1 Z_2 Y_3 Y_6 X_7'),
        qforte.build_circuit('Y_0 Z_1 Z_2 X_3 X_8 Y_9'),
        qforte.build_circuit('X_0 Z_1 Z_2 X_3 Y_8 Y_9'),
        qforte.build_circuit('Y_0 Z_1 Z_2 Y_3 X_8 X_9'),
        qforte.build_circuit('X_0 Z_1 Z_2 Y_3 Y_8 X_9'),
        qforte.build_circuit('Z_0 Z_4'),
        qforte.build_circuit('Y_0 Z_1 Y_2 Z_4'),
        qforte.build_circuit('X_0 Z_1 X_2 Z_4'),
        qforte.build_circuit('Z_0 Z_5'),
        qforte.build_circuit('Y_0 Z_1 Y_2 Z_5'),
        qforte.build_circuit('X_0 Z_1 X_2 Z_5'),
        qforte.build_circuit('Z_0 Z_6'),
        qforte.build_circuit('Y_0 Z_1 Y_2 Z_6'),
        qforte.build_circuit('X_0 Z_1 X_2 Z_6'),
        qforte.build_circuit('Z_0 Z_7'),
        qforte.build_circuit('Y_0 Z_1 Y_2 Z_7'),
        qforte.build_circuit('X_0 Z_1 X_2 Z_7'),
        qforte.build_circuit('Z_0 Z_8'),
        qforte.build_circuit('Y_0 Z_1 Y_2 Z_8'),
        qforte.build_circuit('X_0 Z_1 X_2 Z_8'),
        qforte.build_circuit('Z_0 Z_9'),
        qforte.build_circuit('Y_0 Z_1 Y_2 Z_9'),
        qforte.build_circuit('X_0 Z_1 X_2 Z_9'),
        qforte.build_circuit('Z_1 Z_2'),
        qforte.build_circuit('Y_1 Y_3'),
        qforte.build_circuit('X_1 X_3'),
        qforte.build_circuit('Y_1 X_2 X_4 Y_5'),
        qforte.build_circuit('X_1 X_2 X_4 X_5'),
        qforte.build_circuit('Y_1 Y_2 Y_4 Y_5'),
        qforte.build_circuit('X_1 Y_2 Y_4 X_5'),
        qforte.build_circuit('Y_1 X_2 X_6 Y_7'),
        qforte.build_circuit('X_1 X_2 X_6 X_7'),
        qforte.build_circuit('Y_1 Y_2 Y_6 Y_7'),
        qforte.build_circuit('X_1 Y_2 Y_6 X_7'),
        qforte.build_circuit('Y_1 X_2 X_8 Y_9'),
        qforte.build_circuit('X_1 X_2 X_8 X_9'),
        qforte.build_circuit('Y_1 Y_2 Y_8 Y_9'),
        qforte.build_circuit('X_1 Y_2 Y_8 X_9'),
        qforte.build_circuit('Z_1 Z_3'),
        qforte.build_circuit('Z_1 Z_4'),
        qforte.build_circuit('Y_1 Z_2 Y_3 Z_4'),
        qforte.build_circuit('X_1 Z_2 X_3 Z_4'),
        qforte.build_circuit('Z_1 Z_5'),
        qforte.build_circuit('Y_1 Z_2 Y_3 Z_5'),
        qforte.build_circuit('X_1 Z_2 X_3 Z_5'),
        qforte.build_circuit('Z_1 Z_6'),
        qforte.build_circuit('Y_1 Z_2 Y_3 Z_6'),
        qforte.build_circuit('X_1 Z_2 X_3 Z_6'),
        qforte.build_circuit('Z_1 Z_7'),
        qforte.build_circuit('Y_1 Z_2 Y_3 Z_7'),
        qforte.build_circuit('X_1 Z_2 X_3 Z_7'),
        qforte.build_circuit('Z_1 Z_8'),
        qforte.build_circuit('Y_1 Z_2 Y_3 Z_8'),
        qforte.build_circuit('X_1 Z_2 X_3 Z_8'),
        qforte.build_circuit('Z_1 Z_9'),
        qforte.build_circuit('Y_1 Z_2 Y_3 Z_9'),
        qforte.build_circuit('X_1 Z_2 X_3 Z_9'),
        qforte.build_circuit('Z_2 Z_3'),
        qforte.build_circuit('Y_2 X_3 X_4 Y_5'),
        qforte.build_circuit('X_2 X_3 Y_4 Y_5'),
        qforte.build_circuit('Y_2 Y_3 X_4 X_5'),
        qforte.build_circuit('X_2 Y_3 Y_4 X_5'),
        qforte.build_circuit('Y_2 X_3 X_6 Y_7'),
        qforte.build_circuit('X_2 X_3 Y_6 Y_7'),
        qforte.build_circuit('Y_2 Y_3 X_6 X_7'),
        qforte.build_circuit('X_2 Y_3 Y_6 X_7'),
        qforte.build_circuit('Y_2 X_3 X_8 Y_9'),
        qforte.build_circuit('X_2 X_3 Y_8 Y_9'),
        qforte.build_circuit('Y_2 Y_3 X_8 X_9'),
        qforte.build_circuit('X_2 Y_3 Y_8 X_9'),
        qforte.build_circuit('Z_2 Z_4'),
        qforte.build_circuit('Z_2 Z_5'),
        qforte.build_circuit('Z_2 Z_6'),
        qforte.build_circuit('Z_2 Z_7'),
        qforte.build_circuit('Z_2 Z_8'),
        qforte.build_circuit('Z_2 Z_9'),
        qforte.build_circuit('Z_3 Z_4'),
        qforte.build_circuit('Z_3 Z_5'),
        qforte.build_circuit('Z_3 Z_6'),
        qforte.build_circuit('Z_3 Z_7'),
        qforte.build_circuit('Z_3 Z_8'),
        qforte.build_circuit('Z_3 Z_9'),
        qforte.build_circuit('Z_4 Z_5'),
        qforte.build_circuit('Y_4 X_5 X_6 Y_7'),
        qforte.build_circuit('X_4 X_5 Y_6 Y_7'),
        qforte.build_circuit('Y_4 Y_5 X_6 X_7'),
        qforte.build_circuit('X_4 Y_5 Y_6 X_7'),
        qforte.build_circuit('Y_4 X_5 X_8 Y_9'),
        qforte.build_circuit('X_4 X_5 Y_8 Y_9'),
        qforte.build_circuit('Y_4 Y_5 X_8 X_9'),
        qforte.build_circuit('X_4 Y_5 Y_8 X_9'),
        qforte.build_circuit('Z_4 Z_6'),
        qforte.build_circuit('Z_4 Z_7'),
        qforte.build_circuit('Z_4 Z_8'),
        qforte.build_circuit('Z_4 Z_9'),
        qforte.build_circuit('Z_5 Z_6'),
        qforte.build_circuit('Z_5 Z_7'),
        qforte.build_circuit('Z_5 Z_8'),
        qforte.build_circuit('Z_5 Z_9'),
        qforte.build_circuit('Z_6 Z_7'),
        qforte.build_circuit('Y_6 X_7 X_8 Y_9'),
        qforte.build_circuit('X_6 X_7 Y_8 Y_9'),
        qforte.build_circuit('Y_6 Y_7 X_8 X_9'),
        qforte.build_circuit('X_6 Y_7 Y_8 X_9'),
        qforte.build_circuit('Z_6 Z_8'),
        qforte.build_circuit('Z_6 Z_9'),
        qforte.build_circuit('Z_7 Z_8'),
        qforte.build_circuit('Z_7 Z_9'),
        qforte.build_circuit('Z_8 Z_9') ]

        coef_vec = [
        +9.830996,
        -0.962661,
        +0.311375,
        +0.311375,
        -0.962661,
        +0.311375,
        +0.311375,
        -1.659208,
        -1.659208,
        -2.349085,
        -2.349085,
        -2.349085,
        -2.349085,
        -2.349085,
        -2.349085,
        +0.256716,
        -0.079112,
        -0.079112,
        -0.079112,
        -0.079112,
        +0.056876,
        -0.056876,
        -0.056876,
        +0.056876,
        +0.045787,
        -0.045787,
        -0.045787,
        +0.045787,
        +0.045787,
        -0.045787,
        -0.045787,
        +0.045787,
        +0.045787,
        -0.045787,
        -0.045787,
        +0.045787,
        +0.157522,
        +0.214398,
        -0.063799,
        -0.063799,
        +0.006346,
        -0.006346,
        -0.006346,
        +0.006346,
        +0.006346,
        -0.006346,
        -0.006346,
        +0.006346,
        +0.006346,
        -0.006346,
        -0.006346,
        +0.006346,
        +0.194528,
        -0.051275,
        -0.051275,
        +0.240315,
        -0.057621,
        -0.057621,
        +0.194528,
        -0.051275,
        -0.051275,
        +0.240315,
        -0.057621,
        -0.057621,
        +0.194528,
        -0.051275,
        -0.051275,
        +0.240315,
        -0.057621,
        -0.057621,
        +0.214398,
        -0.063799,
        -0.063799,
        -0.006346,
        -0.006346,
        -0.006346,
        -0.006346,
        -0.006346,
        -0.006346,
        -0.006346,
        -0.006346,
        -0.006346,
        -0.006346,
        -0.006346,
        -0.006346,
        +0.157522,
        +0.240315,
        -0.057621,
        -0.057621,
        +0.194528,
        -0.051275,
        -0.051275,
        +0.240315,
        -0.057621,
        -0.057621,
        +0.194528,
        -0.051275,
        -0.051275,
        +0.240315,
        -0.057621,
        -0.057621,
        +0.194528,
        -0.051275,
        -0.051275,
        +0.191374,
        +0.007132,
        -0.007132,
        -0.007132,
        +0.007132,
        +0.007132,
        -0.007132,
        -0.007132,
        +0.007132,
        +0.007132,
        -0.007132,
        -0.007132,
        +0.007132,
        +0.186606,
        +0.193738,
        +0.186606,
        +0.193738,
        +0.186606,
        +0.193738,
        +0.193738,
        +0.186606,
        +0.193738,
        +0.186606,
        +0.193738,
        +0.186606,
        +0.260133,
        +0.015926,
        -0.015926,
        -0.015926,
        +0.015926,
        +0.015926,
        -0.015926,
        -0.015926,
        +0.015926,
        +0.212353,
        +0.228280,
        +0.212353,
        +0.228280,
        +0.228280,
        +0.212353,
        +0.228280,
        +0.212353,
        +0.260133,
        +0.015926,
        -0.015926,
        -0.015926,
        +0.015926,
        +0.212353,
        +0.228280,
        +0.228280,
        +0.212353,
        +0.260133
        ]

        He_qubit_hamiltonian = qforte.QuantumOperator()
        for i in range(len(circ_vec)):
            He_qubit_hamiltonian.add_term(coef_vec[i], circ_vec[i])

        # Amplitues from ccsd altered slightly
        T_sq = [
        [(2, 0), -0.000000000],
        [(3, 1), -0.000000000],
        [(2, 3, 1, 0), -0.0250000],
        [(3, 2, 0, 1), -0.0250000],
        [(4, 5, 1, 0), -0.0100000],
        [(5, 4, 0, 1), -0.0100000],
        [(6, 7, 1, 0), -0.0100000],
        [(7, 6, 0, 1), -0.0100000],
        [(8, 9, 1, 0), -0.0100000],
        [(9, 8, 0, 1), -0.0100000]
        ]

        ref = [1,1,0,0,0,0,0,0,0,0]

        myVQEslow = vqe.UCCVQE(ref, T_sq, He_qubit_hamiltonian)
        myVQEslow.do_vqe(maxiter=1000, fast=False)
        slow_Energy = myVQEslow.get_energy()
        # slow_initial_Energy = myVQEslow.get_inital_guess_energy()

        myVQEfast = vqe.UCCVQE(ref, T_sq, He_qubit_hamiltonian)
        myVQEfast.do_vqe(maxiter=1000, fast=True)
        fast_Energy = myVQEfast.get_energy()
        # fast_initial_Energy = myVQEfast.get_inital_guess_energy()

        self.assertAlmostEqual(slow_Energy, fast_Energy)
        self.assertLess(E_fci, slow_Energy)
        self.assertLess(E_fci, fast_Energy)
        self.assertLess(slow_Energy-E_fci, 1.0e-5)
        self.assertLess(fast_Energy-E_fci, 1.0e-5)

if __name__ == '__main__':
    unittest.main()
