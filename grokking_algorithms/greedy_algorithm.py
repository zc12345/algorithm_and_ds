#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  greedy_algorithm.py
@Time          :  2020/03/06 22:18:44
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  set cover problem
'''

def greedy(states_needed, stations):
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states_for_station & states_needed
            if len(covered) > len(states_covered):
                states_covered = covered
                best_station = station
        final_stations.add(best_station)
        states_needed -= states_covered
    return final_stations

if __name__ == "__main__":
    states_needed = set([
        "mt", "wa", "or", "id", "nv", "ut", "ca", "az"
    ])
    stations = {}
    stations["k1"] = set(["id", "nv", "ut"])
    stations["k2"] = set(["id", "wa", "mt"])
    stations["k3"] = set(["or", "nv", "ca"])
    stations["k4"] = set(["nv", "ut"])
    stations["k5"] = set(["ca", "az"])
    res = greedy(states_needed, stations)
    print(res)