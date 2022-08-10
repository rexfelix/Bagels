from random import randint


def main():
    print("""
    세 자리 숫자를 맞추는 게임 입니다.
    추측한 숫자가 맞지만 위치가 틀리면 'Pico',
    숫자도 맞고 자리도 맞으면 'Fermi',
    맞는 숫자가 없으면 'Bagels' 힌트를 제공 합니다.
    기회는 10번 주어 집니다. 행운을 빕니다. 
    """)

    is_On = True

    while is_On:
        answer = randint(100, 999)
        str_answer = str(answer)

        for i in range(0, 10):
            _input = input(f"Guess  #{i + 1}: ")
            int_input = int(_input)
            while int_input < 100 or int_input >= 1000:
                print("세 자리 수를 입력 하세요")
                _input = input(f"Guess again #{i + 1}: ")
                int_input = int(_input)

            out_list = []
            for a, _i in zip(str_answer, _input):
                if a == _i:
                    out_list.append("Fermi")
                elif a in _input:
                    out_list.append("Pico")
                else:
                    out_list.append("")

            out_str = ""
            for s in out_list:
                out_str += str(s) + " "

            if out_str.strip() == "":
                out_str = "Bagels"

            print(f"hint = {out_str}")
            if out_str.strip() == "Fermi Fermi Fermi":
                print("성공!\n훌륭한 추론 입니다!\n")
                isOn = input("계속 하려면 'y', 그만 하려면 아무 키나 입력 하세요: ")
                if isOn.strip() == "y":
                    is_On = True
                    print("새로운 게임을 시작 합니다.")
                else:
                    is_On = False
                    print("플레이 해 주셔서 감사 합니다.")
                break
            elif (out_str.strip() != "Fermi Fermi Fermi") and (i + 1 >= 10):
                print("실패 하셨습니다!\n")
                isOn = input("계속 하려면 'y', 그만 하려면 아나무 키나 입력 하세요: ")
                if isOn == "y":
                    is_On = True
                    print("새로운 게임을 시작 합니다.")
                else:
                    is_On = False
                    print("플레이 해 주셔서 감사 합니다.")
                break


if __name__ == "__main__":
    main()
