"""
Bank renege example

Covers:

- Resources: Resource
- Condition events

Scenario:
  A counter with a random service time and customers who renege. Based on the
  program bank08.py from TheBank tutorial of SimPy 2. (KGM)

"""
from analysis.analyzer import *
from report.reporter import *
from simulation.config import *
from simulation.system import SimSystem
from assets.monitored_resource import MonitoredResource


def main() -> None:
    for j in range(MIN_CAPACITY, MAX_CAPACITY + C_STEPS, C_STEPS):
        for i in range(MIN_NEW_CUSTOMERS, MAX_NEW_CUSTOMERS + STEPS, STEPS):
            sim = SimSystem('Bank Renege')
            customers, counter, total_time = sim.run(i, j)
            report(customers, counter, total_time, j)


def report(customers: list, counter: MonitoredResource, total_time: float, tellers: int) -> None:
    # print_obj_list(customers, 'report')

    report_customers = True
    # Report all the values of the customers
    if report_customers:
        # report_all_by_field_obj(customers, 'wait', tellers)
        # report_all_by_field_obj(customers, 'total_time', tellers)
        # report_all_by_field_obj(customers, 'serving_time', tellers, True, -1.0)
        report_all_by_field_obj(customers, 'status', tellers)
        print ('Tellers: %s, Customers: %s \n' % (tellers, len(customers)))

    report_ts = True
    # Report the events in the queue
    # if report_ts:
        # report_all_by_ts(counter.in_service_event, "Service", total_time)
        # report_all_by_ts(counter.queue_event, "Queue", total_time)


if __name__ == '__main__':
    main()
