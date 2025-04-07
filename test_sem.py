from tests.utils_tests import run_sem_test

# Base skeleton for sem testcase
# def test_(tmp_path):
# # 
#     input_text = """

# """.lstrip()

#     expected_code = 0

#     # Optional user input file (can be empty or contain user input)
#     input_file = tmp_path / "input.txt"
#     input_file.write_text("")  # Empty for this test

#     run_sem_test(str(input_file), input_text, expected_code)



def test_missing_run(tmp_path):
# class Main : Object {
#     run:
#     [|
#     x := 'hola'.
#     _ := x print.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run:">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="String" value="hola"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_code = 31

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_sem_test(str(input_file), input_text, expected_code)

