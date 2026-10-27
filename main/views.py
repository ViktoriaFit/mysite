from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    # Логика калькулятора
    result_text = ""
    if request.method == 'POST':
        try:
            gender = request.POST.get('gender', '').strip().lower()
            age = int(request.POST.get('age', 0))
            weight = float(request.POST.get('weight', 0))
            height = float(request.POST.get('height', 0))
            activity = float(request.POST.get('activity', 1.2))
            goal = request.POST.get('goal', 'keep')

            if gender in ['м', 'm']:
                bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
            else:
                bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

            tdee = bmr * activity

            if goal == 'lose':
                slow = round(tdee * 0.90)
                optimal = round(tdee * 0.85)
                aggressive = round(tdee * 0.75)
                result_text = f"""
                <div style="background: #fff; padding: 15px; border-radius: 8px; margin-top: 15px; border-left: 5px solid #e63946;">
                <b>Ваш базовый обмен (BMR):</b> {round(bmr)} ккал<br>
                <b>Ваш суточный расход (TDEE):</b> {round(tdee)} ккал<br><br>
                <b>Варианты для похудения:</b><br>
                1. Медленный (дефицит < 10%): <b>{slow} ккал</b>. Безопасный и устойчивый результат.<br>
                2. Оптимальный (дефицит 10-20%): <b>{optimal} ккал</b>. Рекомендуемый вариант.<br>
                3. Агрессивный (дефицит > 20%): <b>{aggressive} ккал</b>.<br>
                <span style='color:red;'>⚠️ ВНИМАНИЕ: Агрессивный дефицит не рекомендуется! Это может привести к срыву, потере мышечной массы и замедлению обмена веществ. Лучше выбрать оптимальный или медленный вариант.</span>
                </div>
                """
            elif goal == 'gain':
                surplus = round(tdee * 1.15)
                result_text = f"""
                <div style="background: #fff; padding: 15px; border-radius: 8px; margin-top: 15px; border-left: 5px solid #e63946;">
                <b>Ваш базовый обмен (BMR):</b> {round(bmr)} ккал<br>
                <b>Ваш суточный расход (TDEE):</b> {round(tdee)} ккал<br><br>
                <b>Для набора массы:</b> рекомендуемая норма <b>{surplus} ккал</b> (профицит +15%).<br>
                Совет: набирайте вес постепенно, чтобы избежать лишнего жира.
                </div>
                """
            else:
                result_text = f"""
                <div style="background: #fff; padding: 15px; border-radius: 8px; margin-top: 15px; border-left: 5px solid #e63946;">
                <b>Ваш базовый обмен (BMR):</b> {round(bmr)} ккал<br>
                <b>Ваш суточный расход (TDEE):</b> {round(tdee)} ккал<br><br>
                <b>Для сохранения веса:</b> придерживайтесь вашей нормы <b>{round(tdee)} ккал</b>.
                </div>
                """
        except Exception:
            result_text = "<div style='color:red; margin-top: 15px;'>Пожалуйста, введите корректные данные (числа).</div>"

    html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Виктория Зыкова — Персональный тренер</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #ffffff; color: #333; line-height: 1.6; }}
            
            .hero {{ 
                display: flex; align-items: center; justify-content: center; 
                min-height: 100vh; text-align: center; padding: 20px;
                background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://fitnesskaluga.ru/storage/legacy/Services/25/images/dsc03783.jpg') no-repeat center center/cover;
                background-attachment: fixed;
                color: white;
            }}
            .hero-content {{ max-width: 900px; position: relative; z-index: 2; }}
            .hero h1 {{ font-size: 4.5rem; font-weight: normal; font-family: 'Trebuchet MS', 'Segoe UI', sans-serif; margin-bottom: 20px; letter-spacing: 1px; text-shadow: 2px 2px 10px rgba(0,0,0,0.8); }}
            .hero-titles {{ font-size: 1.4rem; margin-bottom: 40px; text-shadow: 1px 1px 5px rgba(0,0,0,0.8); line-height: 1.4; font-weight: 300; }}
            .hero-titles span {{ display: block; margin-bottom: 5px; }}
            
            .btn {{ display: inline-block; padding: 15px 45px; border-radius: 50px; text-decoration: none; font-weight: 600; font-size: 1.1rem; transition: all 0.3s ease; text-transform: uppercase; background: #e63946; color: white; box-shadow: 0 0 20px rgba(230, 57, 70, 0.6); border: none; }}
            .btn:hover {{ background: #ff4d4d; transform: translateY(-3px); box-shadow: 0 0 30px rgba(255, 77, 77, 0.9); }}

            .section {{ padding: 100px 20px; }}
            .container {{ max-width: 1100px; margin: 0 auto; }}
            .section-title {{ font-size: 2.5rem; text-align: center; margin-bottom: 60px; text-transform: uppercase; color: #222; }}
            .section-title span {{ color: #ff4d4d; }}
            
            .about-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: center; }}
            .about-text h2 {{ font-size: 2.5rem; margin-bottom: 20px; color: #222; }}
            .about-text p {{ font-size: 1.1rem; margin-bottom: 20px; color: #555; }}
            .about-image img {{ width: 100%; border-radius: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); display: block; }}
            .about-list {{ list-style: none; margin-top: 20px; }}
            .about-list li {{ margin-bottom: 10px; font-size: 1.1rem; font-weight: bold; color: #222; }}
            .about-list li::before {{ content: "✓"; color: #ff4d4d; margin-right: 10px; }}

            .bg-light {{ background: #f9f9f9; }}
            
            /* ОБНОВЛЕННЫЕ КАРТОЧКИ ПРОГРАММ С ГРАДИЕНТОМ */
            .programs-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; }}
            .program-card {{ 
                background: linear-gradient(145deg, #ffffff, #f0f0f0); /* Градиент от белого к светло-серому */
                padding: 40px 30px; 
                border-radius: 15px; 
                text-align: center; 
                box-shadow: 5px 5px 15px rgba(0,0,0,0.1), -5px -5px 15px rgba(255,255,255,0.8); /* Объемная тень */
                border: 1px solid rgba(255,255,255,0.5); 
                transition: transform 0.3s, box-shadow 0.3s; 
            }}
            .program-card:hover {{ 
                transform: translateY(-10px); 
                box-shadow: 8px 8px 25px rgba(0,0,0,0.15), -8px -8px 25px rgba(255,255,255,0.9); 
            }}
            .program-card h3 {{ font-size: 1.4rem; margin-bottom: 15px; color: #222; text-transform: uppercase; font-weight: 800; }}
            .program-card p {{ color: #555; font-size: 1rem; }}

            /* БЛОК КАК НАЧАТЬ (ТЕМНЫЕ КАРТОЧКИ) */
            .steps-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px; text-align: center; }}
            .step-card {{ 
                background: #2b2b2b; 
                color: white; 
                padding: 30px 20px; 
                border-radius: 15px; 
                box-shadow: 0 10px 20px rgba(0,0,0,0.2); 
                transition: transform 0.3s;
            }}
            .step-card:hover {{
                transform: translateY(-5px);
            }}
            .step-number {{ font-size: 3rem; font-weight: 900; color: #ff4d4d; margin-bottom: 10px; }}
            .step-title {{ font-size: 1.2rem; font-weight: bold; margin-bottom: 10px; color: white; }}
            .step-text {{ color: #cccccc; font-size: 0.95rem; }}

            .footer {{ background: #222; color: white; text-align: center; padding: 50px 20px; }}
            .footer p {{ margin-bottom: 10px; font-size: 1.1rem; }}
            .footer a {{ color: #ff4d4d; text-decoration: none; }}

            .calc-container {{ max-width: 400px; margin: 40px auto; background: #ffffff; padding: 30px; border-radius: 10px; text-align: center; box-shadow: 0 5px 25px rgba(0,0,0,0.1); }}
            .calc-container input, .calc-container select {{ width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; font-size: 16px; }}
            .calc-container button {{ width: 100%; padding: 12px; background: #e63946; color: white; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; margin-top: 10px; font-weight: bold; }}
            .calc-container button:hover {{ background: #ff4d4d; }}
            .calc-result {{ margin-top: 20px; text-align: left; font-size: 0.95rem; }}

            .whatsapp-btn {{
                display: inline-block;
                background-color: #25D366;
                color: white;
                padding: 15px 30px;
                border-radius: 50px;
                text-decoration: none;
                font-size: 1.2rem;
                font-weight: bold;
                margin-top: 20px;
                box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
                transition: all 0.3s ease;
            }}
            .whatsapp-btn:hover {{
                background-color: #1ebe5d;
                transform: translateY(-3px);
            }}

            @media (max-width: 768px) {{
                .hero h1 {{ font-size: 3rem; }}
                .hero-titles {{ font-size: 1.1rem; }}
                .about-grid {{ grid-template-columns: 1fr; }}
                .steps-grid {{ grid-template-columns: 1fr 1fr; }}
            }}
        </style>
    </head>
    <body>

        <header class="hero">
            <div class="hero-content">
                <h1>Нарисуй своё новое тело</h1>
                <div class="hero-titles">
                    <span>Ваш персональный тренер — Президент Украинской Федерации Фитнеса</span>
                    <span>Заслуженный тренер Украины</span>
                    <span>Мастер спорта международного класса</span>
                    <span style="margin-top: 15px; font-weight: bold;">Онлайн и офлайн</span>
                </div>
                <a href="#programs" class="btn">Выбрать программу</a>
            </div>
        </header>

        <section id="about" class="section">
            <div class="container about-grid">
                <div class="about-image">
                    <img src="https://github.com/ViktoriaFit/mysite/blob/main/my_foto.jpg?raw=true" alt="Виктория Зыкова">
                </div>
                <div class="about-text">
                    <h2>Привет, я Виктория!</h2>
                    <p>Я профессиональный персональный фитнес-тренер с 20+ лет практики и тысячи довольных клиентов.</p>
                    <p>Я разрабатываю программу тренировок для любого возраста, уровня физической подготовленности и состояния здоровья.</p>
                    <p style="margin-top: 20px;"><strong>Вы можете выбрать любую программу, которая подходит под ваши цели:</strong></p>
                    <ul class="about-list">
                        <li>Программа похудения, поддержание или набор мышечной массы</li>
                        <li>Реабилитация, профилактика проблем со сколиозом, грыжами, протрузиями, суставами и прочее</li>
                        <li>Послеродовое восстановление</li>
                    </ul>
                    <p style="margin-top: 20px;">В каждой программе будет дан расчёт калорий под ваши цели и составлен план сбалансированного питания.</p>
                    <p>Тренировки могут проходить как оффлайн непосредственно в зале, так и онлайн.</p>
                </div>
            </div>
        </section>

        <section id="programs" class="section bg-light">
            <div class="container">
                <h2 class="section-title">Выбери <span>программу</span></h2>
                <div class="programs-grid">
                    <div class="program-card"><h3>Снижение и коррекция веса</h3><p>Составление тренировочной программы с учётом вашего состояния здоровья, физической подготовленности, возраста. Расчёт калорийности вашего рациона и сбалансированного питания.</p></div>
                    <div class="program-card"><h3>Реабилитация и профилактика проблем с опорно-двигательным аппаратом</h3><p>Программа тренировок составляется с учётом всех ваших противопоказаний по здоровью.</p></div>
                    <div class="program-card"><h3>Послеродовое восстановление</h3><p>Тренировки для восстановления упругости тела.</p></div>
                    <div class="program-card"><h3>Набор мышечной массы</h3><p>Программа тренировок и сбалансированное меню.</p></div>
                    <div class="program-card"><h3>Спортивная подготовка</h3><p>Если ваша цель — выступления на соревнованиях по фитнесу, составлю план периодизации подготовки к соревнованиям, разработаю питание под разные периоды тренировок.</p></div>
                    <div class="program-card"><h3>Онлайн-ведение</h3><p>Тренировки из любой точки мира с полной поддержкой и контролем.</p></div>
                </div>
            </div>
        </section>

        <section class="section">
            <div class="container">
                <h2 class="section-title">Как <span>начать</span></h2>
                <div class="steps-grid">
                    <div class="step-card">
                        <div class="step-number">01</div>
                        <div class="step-title">Выберите программу</div>
                        <div class="step-text">Ознакомьтесь с вариантами и выберите подходящий.</div>
                    </div>
                    <div class="step-card">
                        <div class="step-number">02</div>
                        <div class="step-title">Выберите дни и часы</div>
                        <div class="step-text">Выберите дни и часы тренировок, которые подходят вам и есть у меня свободные.</div>
                    </div>
                    <div class="step-card">
                        <div class="step-number">03</div>
                        <div class="step-title">Оплатите</div>
                        <div class="step-text">Оплата помесячная за 8 или 12 тренировок.</div>
                    </div>
                    <div class="step-card">
                        <div class="step-number">04</div>
                        <div class="step-title">Начинайте тренироваться</div>
                        <div class="step-text">Присоединяйтесь онлайн или оффлайн и начинайте делать фигуру своей мечты.</div>
                    </div>
                </div>
                <div style="text-align: center; margin-top: 50px;">
                    <a href="https://wa.me/994504466921?text=Здравствуйте,%20хочу%20записаться%20на%20тренировку" class="whatsapp-btn" target="_blank">Записаться в WhatsApp</a>
                </div>
            </div>
        </section>

        <section id="calculator" class="section bg-light">
            <div class="container">
                <h2 class="section-title">Калькулятор <span>калорий</span></h2>
                <div class="calc-container">
                    <form method="post">
                        <input type="text" name="gender" placeholder="Пол (М/Ж)" required>
                        <input type="number" name="age" placeholder="Возраст" required>
                        <input type="number" step="0.1" name="weight" placeholder="Вес (кг)" required>
                        <input type="number" step="0.1" name="height" placeholder="Рост (см)" required>
                        <select name="activity">
                            <option value="1.2">Минимальная активность</option>
                            <option value="1.375">Небольшая активность</option>
                            <option value="1.55">Средняя активность</option>
                            <option value="1.725">Высокая активность</option>
                            <option value="1.9">Очень высокая активность</option>
                        </select>
                        <select name="goal">
                            <option value="lose">Похудеть</option>
                            <option value="keep">Сохранить вес</option>
                            <option value="gain">Набрать массу</option>
                        </select>
                        <button type="submit">Рассчитать</button>
                    </form>
                    
                    <div class="calc-result">
                        {result_text}
                    </div>
                </div>
            </div>
        </section>

        <footer class="footer">
            <h3 style="color: white; margin-bottom: 20px; font-size: 1.5rem;">Свяжитесь со мной</h3>
            <p>Пишите в WhatsApp: <a href="https://wa.me/994504466921?text=Здравствуйте,%20хочу%20записаться%20на%20тренировку" target="_blank" style="color: #25D366; font-weight: bold;">Нажмите, чтобы написать</a></p>
            <p>В любое удобное для вас время.</p>
            <p style="margin-top: 30px; font-size: 0.9rem; color: #888;">© 2026 Виктория Зыкова. Персональный тренер.</p>
        </footer>

    </body>
    </html>
    """
    return HttpResponse(html)
