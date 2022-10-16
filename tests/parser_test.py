import excel
import sys

from src.global_enums import GlobalErrorMessages

##################################################################################################
##########################################LINE TEST###############################################
##################################################################################################


def test_calculation_from_line_addition():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('3+2', window.get_table_widget())
    assert parser.calculation_from_line() == 5.0, GlobalErrorMessages.AdditionOperationError.value


def test_calculation_from_line_subtraction():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('3.5-2', window.get_table_widget())
    assert parser.calculation_from_line() == 1.5, GlobalErrorMessages.SubtractionOperationError.value


def test_calculation_from_line_multiplication():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('2*2.5', window.get_table_widget())
    assert parser.calculation_from_line() == 5.0, GlobalErrorMessages.MultiplicationOperationError.value


def test_calculation_from_line_division():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('3/0', window.get_table_widget())
    msg = excel.MessageBox()
    assert parser.calculation_from_line() == msg.dividing_by_zero(), GlobalErrorMessages.DivisionOperationError.value


def test_calculation_from_line_exponentiation():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('2^3', window.get_table_widget())
    assert parser.calculation_from_line() == 8.0, GlobalErrorMessages.ExponentiantOperationError.value


def test_comparing_from_line_max():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('max(3, 2)', window.get_table_widget())
    assert parser.comparing_from_line() == 3.0, GlobalErrorMessages.MaxOperationError.value


def test_comparing_from_line_min():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('min(-3.7, 2)', window.get_table_widget())
    assert parser.comparing_from_line() == -3.7, GlobalErrorMessages.MinOperationError.value

##################################################################################################
####################################SIMPLE CELL TEST##############################################
##################################################################################################


def test_calculation_from_cell_addition_simple():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('=3+2', window.get_table_widget())
    assert parser.calculation_from_cell() == 5.0, GlobalErrorMessages.AdditionOperationError.value


def test_calculation_from_cell_subtraction_simple():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('=3.5-2', window.get_table_widget())
    assert parser.calculation_from_cell() == 1.5, GlobalErrorMessages.SubtractionOperationError.value


def test_calculation_from_cell_multiplication_simple():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('=2*2.5', window.get_table_widget())
    assert parser.calculation_from_cell() == 5.0, GlobalErrorMessages.MultiplicationOperationError.value


def test_calculation_from_cell_division_simple():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('=3/0', window.get_table_widget())
    msg = excel.MessageBox()
    assert parser.calculation_from_cell() == msg.dividing_by_zero(), GlobalErrorMessages.DivisionOperationError.value


def test_calculation_from_cell_exponentiation_simple():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('=2^-2', window.get_table_widget())
    assert parser.calculation_from_cell() == 0.25, GlobalErrorMessages.ExponentiantOperationError.value


def test_comparing_from_cell_max_simple():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('=max(3, 2)', window.get_table_widget())
    assert parser.comparing_from_cell() == 3.0, GlobalErrorMessages.MaxOperationError.value


def test_comparing_from_cell_min_simple():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('=min(-3.7, 2)', window.get_table_widget())
    assert parser.comparing_from_cell() == -3.7, GlobalErrorMessages.MinOperationError.value

##################################################################################################
####################################ADVANCED CELL TEST############################################
##################################################################################################


def test_calculation_from_cell_addition_advanced():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    cellB1 = excel.Cell(0, 1, window.get_table_widget())
    cellC3 = excel.Cell(2, 2, window.get_table_widget())
    cellB1.fill_cell(str(5))
    cellC3.fill_cell(str(-2))
    parser = excel.Parser('=-B1+C3', window.get_table_widget())
    assert parser.calculation_from_cell() == -7.0, GlobalErrorMessages.AdditionOperationError.value


def test_calculation_from_cell_subtraction_advanced():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    cellB1 = excel.Cell(0, 1, window.get_table_widget())
    cellC3 = excel.Cell(2, 2, window.get_table_widget())
    cellB1.fill_cell(str(5))
    cellC3.fill_cell(str(-2))
    parser = excel.Parser('=-B1-C3', window.get_table_widget())
    assert parser.calculation_from_cell() == -3.0, GlobalErrorMessages.SubtractionOperationError.value


def test_calculation_from_cell_multiplication_advanced():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    cellB1 = excel.Cell(0, 1, window.get_table_widget())
    cellC3 = excel.Cell(2, 2, window.get_table_widget())
    cellB1.fill_cell(str(5))
    cellC3.fill_cell(str(-2))
    parser = excel.Parser('=B1*C3', window.get_table_widget())
    assert parser.calculation_from_cell() == -10.0, GlobalErrorMessages.MultiplicationOperationError.value


def test_calculation_from_cell_division_advanced():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    cellB1 = excel.Cell(0, 1, window.get_table_widget())
    cellC3 = excel.Cell(2, 2, window.get_table_widget())
    cellB1.fill_cell(str(5))
    cellC3.fill_cell(str(-2))
    parser = excel.Parser('=-B1/C3', window.get_table_widget())
    assert parser.calculation_from_cell() == 2.5, GlobalErrorMessages.DivisionOperationError.value


def test_calculation_from_cell_exponentiation_advanced():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    cellB1 = excel.Cell(0, 1, window.get_table_widget())
    cellC3 = excel.Cell(2, 2, window.get_table_widget())
    cellB1.fill_cell(str(2))
    cellC3.fill_cell(str(2))
    parser = excel.Parser('=-B1^C3', window.get_table_widget())
    assert parser.calculation_from_cell() == 4.0, GlobalErrorMessages.ExponentiantOperationError.value


def test_comparing_from_cell_max_advanced():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    msg = excel.MessageBox()
    cellB1 = excel.Cell(0, 1, window.get_table_widget())
    cellC3 = excel.Cell(2, 2, window.get_table_widget())
    cellB1.fill_cell(str(5))
    cellC3.fill_cell(str(-2))
    parser = excel.Parser('=max(B1,C3)', window.get_table_widget())
    assert parser.comparing_from_cell() == 5.0, GlobalErrorMessages.MaxOperationError.value


def test_comparing_from_cell_min_advanced():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    cellB1 = excel.Cell(0, 1, window.get_table_widget())
    cellC3 = excel.Cell(2, 2, window.get_table_widget())
    cellB1.fill_cell(str(5))
    cellC3.fill_cell(str(-2))
    parser = excel.Parser('=min(B1, C3)', window.get_table_widget())
    assert parser.comparing_from_cell() == -2.0, GlobalErrorMessages.MinOperationError.value

##################################################################################################
##########################################CELL REPLACMENT#########################################
##################################################################################################


def test_replacement():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    cell = excel.Cell(0, 1, window.get_table_widget())
    cell.fill_cell(str(5))
    parser = excel.Parser('#B1', window.get_table_widget())
    parser2 = excel.Parser('#B3', window.get_table_widget())
    parser3 = excel.Parser('#b3', window.get_table_widget())
    msg = excel.MessageBox()
    assert float(parser.replacement()) == 5.0, GlobalErrorMessages.ReplacementError.value
    assert float(parser2.replacement()) == 0.0, GlobalErrorMessages.ReplacementError.value
    assert float(parser3.replacement()) == msg.incorrect_expression(), GlobalErrorMessages.ReplacementError.value

##################################################################################################
################################LINE CALCULATION RETURN NONE######################################
##################################################################################################


def test_calculation_from_line_none():
    application = excel.QtWidgets.QApplication(sys.argv)
    window = excel.Excel()
    parser = excel.Parser('C+3', window.get_table_widget())
    assert parser.calculation_from_line() is None, GlobalErrorMessages.AdditionOperationError.value


