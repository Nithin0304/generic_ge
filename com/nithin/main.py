import datetime
import sys
import great_expectations as ge
import great_expectations.jupyter_ux
from great_expectations.checkpoint import LegacyCheckpoint
from great_expectations.data_context.types.resource_identifiers import ValidationResultIdentifier
from utils.create_expectations.get_expectations import create_expectation_suite_util
from utils.build_docs.get_data_docs import create_data_docs_util
from handle_errors.args_error import handle_args_error
from pyhocon import ConfigFactory

def main(args):
     if len(args) != 2:
          handle_args_error()
     context = ge.data_context.DataContext()
     conf = ConfigFactory.parse_file(args[1])
     expectation_suite_name = conf.get('expectation_suite_name')
     suite = context.get_expectation_suite(expectation_suite_name)
     suite.expectations = []
     batch_kwargs = conf.get('batch_kwargs')
     batch = context.get_batch(batch_kwargs, suite)
     batch.head()
     expectations = conf.get('expectations')
     create_expectation_suite_util(expectations,batch)
     batch.save_expectation_suite(discard_failed_expectations=False)
     create_data_docs_util(context,conf)

if __name__ == '__main__':
     main(sys.argv)






                
    
    