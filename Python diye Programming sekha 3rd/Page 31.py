def average(L):
    if not L:
        return None
    return sum(L)/len(L)

def test_average():
    test_cases=[
        {
            "name":"simple case 1",
            "input":[1,2,3],
            "expected":2.0
        },
        {"name":"simple case 2",
         "input":[1,2,3,4],
         "expected":2.0
         },
        {"name":"list with one item",
         "input":[100],
         "expected":100.0
         },
        {"name":"empty list",
         "input":[],
         "expected":None
         }

    ]


    for  test_case in test_cases:
        assert test_case["expected"]==average(test_case["input"]),test_case["name"]

"""Output:
pytest Main.py
================================================= test session starts =================================================
platform win32 -- Python 3.8.3, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\Dell\Desktop
collected 1 item

Main.py F                                                                                                        [100%]

====================================================== FAILURES =======================================================
____________________________________________________ test_average _____________________________________________________

    def test_average():
        test_cases=[
            {
                "name":"simple case 1",
                "input":[1,2,3],
                "expected":2.0
            },
            {"name":"simple case 2",
             "input":[1,2,3,4],
             "expected":2.0
             },
            {"name":"list with one item",
             "input":[100],
             "expected":100.0
             },
            {"name":"empty list",
             "input":[],
             "expected":None
             }

        ]


        for  test_case in test_cases:
>           assert test_case["expected"]==average(test_case["input"]),test_case["name"]
E           AssertionError: simple case 2
E           assert 2.0 == 2.5
E            +  where 2.5 = average([1, 2, 3, 4])

Main.py:30: AssertionError
=============================================== short test summary info ===============================================
FAILED Main.py::test_average - AssertionError: simple case 2
================================================== 1 failed in 0.26s =================================================="""