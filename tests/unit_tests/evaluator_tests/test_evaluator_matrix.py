import math

from evaluator.evaluator_matrix import EvaluatorMatrix
from tests.test_utils.config import load_test_config
from config.cst import EvaluatorMatrixTypes


def _get_tools():
    config = load_test_config()
    matrix_inst = EvaluatorMatrix(config)
    matrix = matrix_inst.matrix
    return matrix_inst, matrix, config


def test_init():
    matrix_inst, matrix, config = _get_tools()
    assert EvaluatorMatrixTypes.TA in matrix
    assert EvaluatorMatrixTypes.SOCIAL in matrix
    assert EvaluatorMatrixTypes.REAL_TIME in matrix
    assert EvaluatorMatrixTypes.STRATEGIES in matrix


def test_set_get_eval():
    matrix_inst, matrix, config = _get_tools()
    values = [1, 1.02, math.pi, math.nan]
    for value in values:
        for matrix_type in EvaluatorMatrixTypes:
            key = "{}{}".format(matrix_type, value)
            matrix_inst.set_eval(matrix_type, key, value)
            if math.isnan(value):
                assert matrix_inst.get_eval_note(matrix, matrix_type, key) is None
            else:
                assert matrix_inst.get_eval_note(matrix, matrix_type, key) == value
