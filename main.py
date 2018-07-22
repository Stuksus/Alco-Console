
import os
error = 0
mainText= """Выберете желаемы результат из предложенных:
    1. В целом нормальное состояние, наличие алкоголя в крови определяется только специальными тестами
    2. Легкая эйфория, чувство расслабления, радости, повышенная общительность, разговорчивость, нарушение концентрации внимания
    3. Экстравертность, расторможенность, неестественное веселье, притупление ощущений, нарушается периферическое зрение, глубина восприятия, рассуждения становятся бессвязными
    4. Экспрессивность, необоснованная агрессия, эмоциональная лабильность, снижение либидо, нарушение равновесия (шатающаяся походка), нечленораздельная речь, нарушение рефлексов, замедленная реакция, самопроизвольная эрекция
    5. Теряется понимание, состояние ступора, потеря ощущений, возможно, потеря сознания, памяти, нарушение моторики
    6. Сильнейшее угнетение ЦНС, потеря сознания (неконтролируемое мочеиспускание, утрата чувства равновесия, нарушение сердцебиения и дыхания), возникает угроза смерти
    7. Полная потеря контроля за своим поведением, потеря сознания, риск смерти (нарушение дыхания, сердцебиения, нистагм)
    8. Cильнейшее отравление и летальногый исход
"""

mass = float((input("Введите Ваш вес:")))
choiceGender = """Выберите свой пол:
1. Мужской
2. Женский
"""
print(choiceGender)
while True:
    pointGender = int(input("Введите выбранный пункт: "))
    if pointGender == 1:
        gender= 0.7
        break
    elif pointGender == 2:
        gender = 0.6
        break
    else:
        print("Вы выбрали не существующий пункт, попробуйте снова")
        error+=1
        if error == 3:
            print("Попробуйте еще раз, вы сможете, мы в вас верим")
        elif error ==4:
            print("Мы поняли! Вы являетесь Сверхчеловекм, поэтому пол для вас не существенен\n")
            gender = 0.65
            break


dosa = [0.1,0.29,0.3,0.59,0.6,0.99,1,1.99,2,2.99,3,3.99,4,5,5,7]
def Widmark(dosamin,dosamax,mass,gender,digree):
    density = 0.79
    volumemin = ((dosamin*mass*gender/digree)/density)*1.1
    volumemax = ((dosamax*mass*gender/digree)/density)*1.1

    print("Максимальное количество алкоголя для достижения выбранного Вами результата: ",round(volumemax),"мл")
    print("Минимальное количество алкоголя для достижения выбранного Вами результата: ",round(volumemin),"мл")

digree = float((input("Введите градус вашего напитка: ")))/100
print(mainText)
while True:
    pointStatus = int(input("Введите выбранный пункт: "))
    if pointStatus == 1:
        Widmark(dosa[0],dosa[1],mass,gender,digree)
        break
    elif pointStatus == 2:
        Widmark(dosa[2], dosa[3], mass, gender, digree)
        break
    elif pointStatus == 3:
        Widmark(dosa[4], dosa[5], mass, gender, digree)
        break
    elif pointStatus == 4:
        Widmark(dosa[6], dosa[7], mass, gender, digree)
        break
    elif pointStatus == 5:
        Widmark(dosa[8], dosa[9], mass, gender, digree)
        break
    elif pointStatus == 6:
        Widmark(dosa[10], dosa[11], mass, gender, digree)
        break
    elif pointStatus == 7:
        Widmark(dosa[12], dosa[13], mass, gender, digree)
        break
    elif pointStatus == 8:
        Widmark(dosa[14], dosa[15], mass, gender, digree)
        break
    else:
        error+=1
        print(error)
        if error <5:
            print("Возможно вы уже пьяны или выбрали не существующий пункт, попробуйте снова")
        elif error == 5:
            print("Мы думаем, что вы уже изрядно пьяны, мы бы посоветовали вам не употреблять алкоголь в течение следующих 6 часов")
        elif error == 6:
            print("К сожалению, наша совесть не позволяет нам далее работать с Вами, поэтому мы вынуждены разорвать соединение и не реагировать на ваши запросы в течении 6 часов")
            break

os.system("pause")