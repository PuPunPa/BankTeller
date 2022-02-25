from analysis.analyzer import *
from simulation.config import *
from assets.status import Status
from scipy.stats import norm


def report_all_by_field_obj(my_objs: list, my_field: str, tellers: int, w_filter: bool = False, val: float = 0.0) -> float:
    print('\n === Report for %s field ===' % my_field)
    is_status = isinstance(getattr(my_objs[0], my_field), Status)
    if not is_status:
        max_time = get_max_obj(my_objs, my_field, w_filter, val)
        min_time = get_min_obj(my_objs, my_field, w_filter, val)
        max_list = get_matching_value_obj(my_objs, my_field, max_time)
        min_list = get_matching_value_obj(my_objs, my_field, min_time)
        min_perc = len(min_list)/len(my_objs)
        # field_list = get_map_values(my_objs, my_field)
        mean = get_mean_obj(my_objs, my_field, w_filter, val)
        median = get_median_obj(my_objs, my_field, w_filter, val)
        std = get_stdev_obj(my_objs, my_field, w_filter, val)
        variance = get_variance_obj(my_objs, my_field, w_filter, val)
        one_std_list = list(x for x in get_map_values(my_objs, my_field) if (mean-std) <= x <= (mean+std))
        one_std_list = list(dict.fromkeys(one_std_list))
        
        plt.xlabel('%s' % my_field)
        plt.ylabel("Probability Density")
        x_axis = np.arange(min_time, max_time, 0.01)
        plt.plot(x_axis, norm.pdf(x_axis, mean, std))
        plt.fill_between(x_axis, norm.pdf(x_axis, mean, std), 0,alpha = 0.2, color = 'blue')
        x_axis = np.arange(min(one_std_list), max(one_std_list), 0.01)
        plt.plot(x_axis, norm.pdf(x_axis, mean, std))
        plt.fill_between(x_axis, norm.pdf(x_axis, mean, std), 0,alpha = 0.5, color = 'red')
        plt.title('%s Tellers, %s Clients' % (tellers, len(my_objs)))
        plt.show()
        
        
        print('Max %s: %5.3f by %s' %
              (my_field, max_time, objects_as_str(max_list)))
        print('Min %s: %5.3f by %s' %
              (my_field, min_time, objects_as_str(min_list)))
        print('Percentage of Min %s: %5.3f' % (my_field, min_perc))
        print('Mean %s: %5.3f' % (my_field, mean))
        print('Median %s: %5.3f' % (my_field, median))
        print('Within One Stdev: %s' % objects_as_str(get_matching_values(my_objs, my_field, one_std_list)))
        try:
            print('Mode %s: %5.3f' % (my_field, get_mode_obj(my_objs, my_field, w_filter, val)))
        except Exception:
            print('No mode found in data')
        print('Stdev %s: %5.3f' % (my_field, std))
        print('Variance %s: %5.3f' % (my_field, variance))
        return 0
    else:
        # print(is_status)
        values = get_map_values(my_objs, my_field)
        # print(values)
        suc = get_matching_value_obj(values, 'name', 'SUCCESS')
        suc_rate = len(suc)/len(values)
        print('Success Rate: %5.3f' % suc_rate)
        return suc_rate
        # TODO: get a histogram count on every status
        # TODO: graph the histogram
        # these 3 are what we did in class with the excell sheet


def report_all_by_ts(my_ts: list, my_label: str, total_time: float) -> None:
    print('\n === Report for %s resource ===' % my_label)
    if my_ts:
        # print_ts(my_ts, my_label)
        # print('Min queue: %4.3f' % get_min_ts(my_ts))
        print('Max queue: %4.3f' % get_max_ts(my_ts))
        service_vals = get_cumulative_time_ts(my_ts, total_time)
        percent_vals = get_bin_percent_ts(service_vals, total_time, my_label)
        if CREATE_SIM_GRAPHS:
            plot_ts(my_ts, total_time, my_label)
            evolution_bar_ts(my_ts, total_time, my_label)
            cumulative_time_ts(service_vals, my_label)
            hist_bar_ts(my_ts, 'value', my_label)
    else:
        print('%s not used' % my_label)