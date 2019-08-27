import unittest
from tests.test_models import VerifySwapiConfig
from tests.test_models import VerifyStarship
from tests.test_models import VerifyPilot
from tests.test_models import VerifyStarship
from tests.test_dependences import VerifyDependences
from tests.test_services import VerifySwapiService
from tests.test_utils import VerifyUtils
from tests.test_utils import VerifyUtils
from tests.test_controllers import VerifySwapiController

def suite():
    suite = unittest.TestSuite()

    suite.addTest(VerifySwapiConfig('test_instance_property'))
    suite.addTest(VerifySwapiConfig('test_instance_values_correct'))

    suite.addTest(VerifyStarship('test_instance_property'))
    suite.addTest(VerifyStarship('test_instance_values_correct'))
    
    suite.addTest(VerifyPilot('test_instance_property'))
    suite.addTest(VerifyPilot('test_instance_values_correct'))

    suite.addTest(VerifyDependences('import_all_modules'))

    suite.addTest(VerifySwapiService('test_instance_property'))
    suite.addTest(VerifySwapiService('test_functions'))
    suite.addTest(VerifySwapiService('test_request'))

    suite.addTest(VerifyUtils('find_numeric_values'))

    suite.addTest(VerifySwapiController('test_instance_property'))
    suite.addTest(VerifySwapiController('test_run_command'))
    suite.addTest(VerifySwapiController('test_fill_starship'))
    suite.addTest(VerifySwapiController('test_fill_pilot'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())