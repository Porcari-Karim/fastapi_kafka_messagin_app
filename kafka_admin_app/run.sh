#!/bin/bash

exec python3 ./admin_creator_listener.py &
exec python3 ./admin_deleter_listener.py &
exec python3 ./admin_population_checker.py