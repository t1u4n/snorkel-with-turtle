from alert.alert_system import AlertSystem
from logging import DEBUG


def test_alert_functionality():
    alert_sys = AlertSystem()
    alert_sys.alert("This is a debug message", DEBUG)