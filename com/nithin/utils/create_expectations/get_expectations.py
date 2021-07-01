def create_expectation_suite_util(expectations,batch):
 for expectation in expectations:
     if expectation.type == 'expect_column_to_exist':
          for columns in expectation.columns:
                    batch.expect_column_to_exist(column = columns)
     elif expectation.type == 'expect_table_row_count_to_be_between':
          batch.expect_table_row_count_to_be_between(max_value=expectation.max_value,min_value=expectation.min_value)
     elif expectation.type == 'expect_table_columns_to_match_ordered_list':
          batch.expect_table_columns_to_match_ordered_list(column_list = expectation.columns)
     elif expectation.type == 'expect_table_columns_to_match_set':
          batch.expect_table_columns_to_match_set(column_set = expectation.columns)
     elif expectation.type == 'expect_table_row_count_to_equal':
          batch.expect_table_row_count_to_equal(value = expectation.value)
     elif expectation.type == 'expect_table_column_count_to_be_between':
          batch.expect_table_column_count_to_be_between(min_value = expectation.min_value,max_value = expectation.max_value)
     elif expectation.type == 'expect_table_column_count_to_equal':
          batch.expect_table_column_count_to_equal(value = expectation.value)
     elif expectation.type == 'expect_column_values_to_be_unique':
          batch.expect_column_values_to_be_unique(column = expectation.column, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_not_be_null':
          batch.expect_column_values_to_not_be_null(column = expectation.column, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_be_null':
          batch.expect_column_values_to_be_null(column = expectation.column, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_be_of_type':
          batch.expect_column_values_to_be_of_type(column = expectation.column, type_ = expectation.type, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_be_in_type_list':
          batch.expect_column_values_to_be_in_type_list(column = expectation.column, type_list = expectation.type_list, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_be_in_set':
          batch.expect_column_values_to_be_in_set(column = expectation.column, value_set = expectation.value_set, mostly = expectation.get('mostly') or None, parse_strings_as_datetimes = expectation.get('parse_strings_as_datetimes') or None)
     elif expectation.type == 'expect_column_values_not_to_be_in_set':
          batch.expect_column_values_not_to_be_in_set(column = expectation.column, value_list = expectation.value_list, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_be_between':
          batch.expect_column_values_to_be_between(column=expectation.column,min_value = expectation.min_value,max_value = expectation.max_value, strict_min = expectation.get('strict_min') or False, strict_max = expectation.get('strict_max') or False, parse_strings_as_datetimes = expectation.get('parse_strings_as_datetimes') or None, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_be_increasing':
          batch.expect_column_values_to_be_increasing(column=expectation.column,strictly=expectation.get('strictly') or None,parse_strings_as_datetimes= expectation.get('parse_strings_as_datetimes') or False,mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_be_decreasing':
          batch.expect_column_values_to_be_decreasing(column=expectation.column,strictly=expectation.get('strictly') or None,parse_strings_as_datetimes= expectation.get('parse_strings_as_datetimes') or False,mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_value_lengths_to_equal':
          batch.expect_column_value_lengths_to_equal(column=expectation.column,value = expectation.value, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_match_regex':
          batch.expect_column_values_to_match_regex(column=expectation.column,regex = expectation.regex, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_not_match_regex':
          batch.expect_column_values_to_not_match_regex(column=expectation.column,regex = expectation.regex, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_match_regex_list':
          batch.expect_column_values_to_match_regex_list(column=expectation.column,regex_list = expectation.regex_list,match_on = expectation.get('match_on') or any, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_not_match_regex_list':
          batch.expect_column_values_to_not_match_regex_list(column=expectation.column,regex_list = expectation.regex_list,match_on = expectation.get('match_on') or any, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_match_strftime_format':
          batch.expect_column_values_to_match_strftime_format(column=expectation.column,strftime_format = expectation.strftime_format,match_on = expectation.get('match_on') or any, mostly = expectation.get('mostly') or None)
     #     elif expectation.type == 'expect_column_values_to_match_strftime_format':
     #          batch.expect_table_row_count_to_equal(column=expectation.columnm, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_match_json_parseable':
          batch.expect_column_values_to_match_json_parseable(column=expectation.columnm, mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_values_to_match_json_schema':
          batch.expect_column_values_to_match_json_schema(column=expectation.column,json_schema= expectation.json_schema,mostly = expectation.get('mostly') or None)
     elif expectation.type == 'expect_column_parameterized_distribution_ks_test_p_value_to_be_greater_than':
          batch.expect_column_parameterized_distribution_ks_test_p_value_to_be_greater_than(column = expectation.column, distribution = expectation.distribution,p_value = expectation.p_value, params = expectation.get('params') or None)
     elif expectation.type == 'expect_column_distinct_values_to_be_in_set':
          batch.expect_column_distinct_values_to_be_in_set(column = expectation.column, value_set = expectation.value_set, parse_strings_as_datetimes = expectation.get('parse_strings_as_datetimes') or None)
     elif expectation.type == 'expect_column_distinct_values_to_equal_set':
          batch.expect_column_distinct_values_to_equal_set(column = expectation.column, value_set = expectation.value_set, parse_strings_as_datetimes = expectation.get('parse_strings_as_datetimes') or None)
     elif expectation.type == 'expect_column_distinct_values_to_contain_set':
          batch.expect_column_distinct_values_to_contain_set(column = expectation.column, value_set = expectation.value_set, parse_strings_as_datetimes = expectation.get('parse_strings_as_datetimes') or None)
     elif expectation.type == 'expect_column_mean_to_be_between':
          batch.expect_column_mean_to_be_between(column=expectation.column,min_value = expectation.min_value,max_value = expectation.max_value, strict_min = expectation.get('strict_min') or False)
     elif expectation.type == 'expect_column_median_to_be_between':
          batch.expect_column_median_to_be_between(column=expectation.column,min_value = expectation.min_value,max_value = expectation.max_value, strict_min = expectation.get('strict_min') or False, strict_max = expectation.get('strict_max') or False)
     #     elif expectation.type == 'expect_column_median_to_be_between':
     #          batch.expect_column_median_to_be_between(column=expectation.column,quantile_ranges = expectation.quantile_ranges, allow_relative_error = expectation.get('allow_relative_error') or False)
     elif expectation.type == 'expect_column_stdev_to_be_between':
          batch.expect_column_stdev_to_be_between(column=expectation.column,min_value = expectation.min_value,max_value = expectation.max_value, strict_min = expectation.get('strict_min') or False, strict_max = expectation.get('strict_max') or False)
     elif expectation.type == 'expect_column_unique_value_count_to_be_between':
          batch.expect_column_unique_value_count_to_be_between(column=expectation.column,min_value = expectation.min_value,max_value = expectation.max_value)
     elif expectation.type == 'expect_column_proportion_of_unique_values_to_be_between':
          batch.expect_column_proportion_of_unique_values_to_be_between(column=expectation.column,min_value = expectation.min_value,max_value = expectation.max_value, strict_min = expectation.get('strict_min') or False, strict_max = expectation.get('strict_max') or False)
     elif expectation.type == 'expect_column_most_common_value_to_be_in_set':
          batch.expect_column_most_common_value_to_be_in_set(column = expectation.column, value_set = expectation.value_set, ties_okay = expectation.get('ties_okay') or None)
     elif expectation.type == 'expect_column_sum_to_be_between':
          batch.expect_column_sum_to_be_between(column=expectation.column,min_value = expectation.min_value,max_value = expectation.max_value, strict_min = expectation.get('strict_min') or False,strict_max = expectation.get('strict_max') or False)
     elif expectation.type == 'expect_column_min_to_be_between':
          batch.expect_column_min_to_be_between(column=expectation.column,min_value = expectation.min_value,max_value = expectation.max_value, strict_min = expectation.get('strict_min') or False,strict_max = expectation.get('strict_max') or False, parse_strings_as_datetimes = expectation.get('parse_strings_as_datetimes') or None, output_strftime_format = expectation.get('output_strftime_format') or None)
     elif expectation.type == 'expect_column_max_to_be_between':
          batch.expect_column_max_to_be_between(column=expectation.column,min_value = expectation.min_value,max_value = expectation.max_value, strict_min = expectation.get('strict_min') or False,strict_max = expectation.get('strict_max') or False, parse_strings_as_datetimes = expectation.get('parse_strings_as_datetimes') or None, output_strftime_format = expectation.get('output_strftime_format') or None)
     elif expectation.type == 'expect_column_sum_to_be_between':
          batch.expect_column_sum_to_be_between(column=expectation.column,min_value = expectation.min_value,max_value = expectation.max_value, strict_min = expectation.get('strict_min') or False,strict_max = expectation.get('strict_max') or False)
     elif expectation.type == 'expect_column_min_to_be_between':
          batch.expect_column_min_to_be_between(column=expectation.column,min_value = expectation.min_value,max_value = expectation.max_value, strict_min = expectation.get('strict_min') or False,strict_max = expectation.get('strict_max') or False, parse_strings_as_datetimes = expectation.get('parse_strings_as_datetimes') or None, output_strftime_format = expectation.get('output_strftime_format') or None)
     elif expectation.type == 'expect_column_max_to_be_between':
          batch.expect_column_max_to_be_between(column=expectation.column,min_value = expectation.min_value,max_value = expectation.max_value, strict_min = expectation.get('strict_min') or False,strict_max = expectation.get('strict_max') or False, parse_strings_as_datetimes = expectation.get('parse_strings_as_datetimes') or None, output_strftime_format = expectation.get('output_strftime_format') or None)