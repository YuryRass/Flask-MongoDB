#!/bin/bash
# Скрипт мониторит потребление CPU и оперативной памяти

while :
do 
  # Получение текущей информации о потреблении CPU и операт. памяти
  cpuUsage=$(top -bn1 | awk '/Cpu/ { print $2}')
  memUsage=$(free -m | awk '/Mem/{print $3}')

  # Вывод результата
  echo "CPU Usage: $cpuUsage%"
  echo "Memory Usage: $memUsage MB"
 
  # Сон на 1 секунду
  sleep 1
done
