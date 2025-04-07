from tests.utils_tests import run_test

# Base skeleton for testcase
# def test_(tmp_path):
#     input_text = """

# """.lstrip()

#     expected_output = ""

#     # Optional user input file (can be empty or contain user input)
#     input_file = tmp_path / "input.txt"
#     input_file.write_text("")  # Empty for this test

#     run_test(str(input_file), input_text, expected_output)


def test_basic_output(tmp_path):
# class Main : Object {
#     run
#     [|
#     x := 'hola'.
#     _ := x print.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
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

    expected_output = "hola"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_basic_int_output(tmp_path):
# class Main : Object {
#     run
#     [|
#     x := 5.
#     y := x asString.
#     _ := y print.
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="Integer" value="5"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="asString">
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "5"

    # Optional user input file (can be empty or contain something later)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)

def test_plus(tmp_path):
# class Main : Object {
#     run
#     [|
#     x := 5.
#     y := x plus: 2.
#     x := y asString.
#     _ := x print.
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="Integer" value="5"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="2"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="x"/>
                    <expr>
                        <send selector="asString">
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
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

    expected_output = "7"

    # Optional user input file (can be empty or contain something later)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)

def test_all_basic_math(tmp_path):
# class Main : Object {
#     run
#     [|
#     x := 5.
#     y := x minus: 2.
#     x := y multiplyBy: 4.
#     y := x divBy: 3.
#     _ := (y asString) print.
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="Integer" value="5"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="minus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="2"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="x"/>
                    <expr>
                        <send selector="multiplyBy:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="4"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="y"/>
                    <expr>
                        <send selector="divBy:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="3"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="y"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "4"

    # Optional user input file (can be empty or contain something later)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)

def test_read(tmp_path):
# class Main : Object {
#     run
#     [|
#     x := String read.
#     _ := x print.
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="read">
                            <expr>
                                <literal class="class" value="String"/>
                            </expr>
                        </send>
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

    expected_output = "ahoj"

    # Optional user input file (can be empty or contain something later)
    input_file = tmp_path / "input.txt"
    input_file.write_text("ahoj")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)

def test_block_result(tmp_path):
# class Main : Object {
# run [|
#     a := self foo: 4.
#     _ := (a asString) print.
#     b := [ :x | _ := 42. ].
#     c := b value: 16.
#     _ := (c asString) print.
#     d := 'ahoj' print .
#     _ := d print.
# ]
# foo: [ :x |
#     u := x plus: 10.
# ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="a"/>
                    <expr>
                        <send selector="foo:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="4"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="a"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="b"/>
                    <expr>
                        <block arity="1">
                            <parameter order="1" name="x"/>
                            <assign order="1">
                                <var name="_"/>
                                <expr>
                                    <literal class="Integer" value="42"/>
                                </expr>
                            </assign>
                        </block>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="c"/>
                    <expr>
                        <send selector="value:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="16"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="b"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="c"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="d"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <literal class="String" value="ahoj"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="7">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="d"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
        <method selector="foo:">
            <block arity="1">
                <parameter order="1" name="x"/>
                <assign order="1">
                    <var name="u"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="10"/>
                                </expr>
                            </arg>
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

    expected_output = "1442ahojahoj"

    # Optional user input file (can be empty or contain something later)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_method_redefinition(tmp_path):
# class Main : Object {
#     run
#     [|
#         x := MyInt from: 5.
#         y := x plus: 10.
#         x := y multiplyBy: 5.
#         _ := (x asString) print.
#     ]
# }

# class MyInt : Integer {
#     multiplyBy:
#     [ :x| 
#         r := self minus: x.
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="5"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="10"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="x"/>
                    <expr>
                        <send selector="multiplyBy:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="5"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
    <class name="MyInt" parent="Integer">
        <method selector="multiplyBy:">
            <block arity="1">
                <parameter order="1" name="x"/>
                <assign order="1">
                    <var name="r"/>
                    <expr>
                        <send selector="minus:">
                            <arg order="1">
                                <expr>
                                    <var name="x"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "10"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)




# def test_(tmp_path):
#     input_text = """

# """.lstrip()

#     expected_output = ""

#     # Optional user input file (can be empty or contain user input)
#     input_file = tmp_path / "input.txt"
#     input_file.write_text("")  # Empty for this test

#     run_test(str(input_file), input_text, expected_output)



# def test_(tmp_path):
#     input_text = """

# """.lstrip()

#     expected_output = ""

#     # Optional user input file (can be empty or contain user input)
#     input_file = tmp_path / "input.txt"
#     input_file.write_text("")  # Empty for this test

#     run_test(str(input_file), input_text, expected_output)





def test_example(tmp_path):
# class Main : Object {
#     run "<- definice metody - bezparametrický selektor run"
#     [ |
#         x := self compute: 3 and: 2 and: 5.
#         x := self plusOne: (self vysl).
#         y := x asString .
#         _ := y print.
#     ]
    
#     plusOne: 
#     [ :x | 
#         r := x plus: 1. 
#     ]
    
#     compute:and:and: 
#     [ :x :y :z |    
#         a := x plus: y.
#         _ := self vysl: a.
#         _ := (( self vysl) greaterThan: 0)
#         ifTrue: [|u := self vysl: 1.]
#         ifFalse: [|].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25" description="&lt;- definice metody - bezparametrický selektor run">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="compute:and:and:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="3"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <literal class="Integer" value="2"/>
                                </expr>
                            </arg>
                            <arg order="3">
                                <expr>
                                    <literal class="Integer" value="5"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="x"/>
                    <expr>
                        <send selector="plusOne:">
                            <arg order="1">
                                <expr>
                                    <send selector="vysl">
                                        <expr>
                                            <var name="self"/>
                                        </expr>
                                    </send>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="y"/>
                    <expr>
                        <send selector="asString">
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
        <method selector="plusOne:">
            <block arity="1">
                <parameter order="1" name="x"/>
                <assign order="1">
                    <var name="r"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
        <method selector="compute:and:and:">
            <block arity="3">
                <parameter order="1" name="x"/>
                <parameter order="2" name="y"/>
                <parameter order="3" name="z"/>
                <assign order="1">
                    <var name="a"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <var name="y"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="_"/>
                    <expr>
                        <send selector="vysl:">
                            <arg order="1">
                                <expr>
                                    <var name="a"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="self"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="u"/>
                                            <expr>
                                                <send selector="vysl:">
                                                    <arg order="1">
                                                        <expr>
                                                            <literal class="Integer" value="1"/>
                                                        </expr>
                                                    </arg>
                                                    <expr>
                                                        <var name="self"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0"/>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="greaterThan:">
                                    <arg order="1">
                                        <expr>
                                            <literal class="Integer" value="0"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <send selector="vysl">
                                            <expr>
                                                <var name="self"/>
                                            </expr>
                                        </send>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "2"

    # Optional user input file (can be empty or contain something later)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)
