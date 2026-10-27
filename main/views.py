from django.http import HttpResponse

def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Виктория Зыкова — Персональный тренер</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #ffffff; color: #333; line-height: 1.6; }
            
            /* --- ГЛАВНЫЙ ЭКРАН --- */
            .hero { 
                display: flex; align-items: center; justify-content: center; 
                min-height: 100vh; text-align: center; padding: 20px;
                background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://fitnesskaluga.ru/storage/legacy/Services/25/images/dsc03783.jpg') no-repeat center center/cover;
                background-attachment: fixed;
                color: white;
            }
            
            .hero-content { max-width: 900px; position: relative; z-index: 2; }
            
            /* ЛЁГКИЙ СОВРЕМЕННЫЙ ШРИФТ БЕЗ ЗАСЕЧЕК — TREBUCHET MS */
            .hero h1 { 
                font-size: 4.5rem; 
                font-weight: normal; 
                font-family: 'Trebuchet MS', 'Segoe UI', sans-serif;
                margin-bottom: 20px; 
                letter-spacing: 1px;
                text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
            }
            
            .hero-titles { 
                font-size: 1.4rem; 
                margin-bottom: 40px; 
                text-shadow: 1px 1px 5px rgba(0,0,0,0.8);
                line-height: 1.4;
                font-weight: 300;
            }
            .hero-titles span { display: block; margin-bottom: 5px; }
            
            /* КРАСНАЯ КНОПКА */
            .btn { 
                display: inline-block; 
                padding: 15px 45px; 
                border-radius: 50px; 
                text-decoration: none; 
                font-weight: 600; 
                font-size: 1.1rem;
                transition: all 0.3s ease; 
                text-transform: uppercase;
                background: #e63946; 
                color: white;
                box-shadow: 0 0 20px rgba(230, 57, 70, 0.6); 
                border: none;
            }
            .btn:hover { 
                background: #ff4d4d; 
                transform: translateY(-3px); 
                box-shadow: 0 0 30px rgba(255, 77, 77, 0.9);
            }

            /* --- ОСТАЛЬНЫЕ СЕКЦИИ --- */
            .section { padding: 100px 20px; }
            .container { max-width: 1100px; margin: 0 auto; }
            .section-title { font-size: 2.5rem; text-align: center; margin-bottom: 60px; text-transform: uppercase; color: #222; }
            .section-title span { color: #ff4d4d; }
            
            .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: center; }
            .about-text h2 { font-size: 2.5rem; margin-bottom: 20px; color: #222; }
            .about-text p { font-size: 1.1rem; margin-bottom: 20px; color: #555; }
            
            .about-image img { width: 100%; border-radius: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); display: block; }
            
            .about-list { list-style: none; margin-top: 20px; }
            .about-list li { margin-bottom: 10px; font-size: 1.1rem; font-weight: bold; color: #222; }
            .about-list li::before { content: "✓"; color: #ff4d4d; margin-right: 10px; }

            .bg-light { background: #f9f9f9; }
            
            .programs-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
            .program-card { background: white; padding: 40px 30px; border-radius: 10px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: transform 0.3s; }
            .program-card:hover { transform: translateY(-5px); }
            .program-card h3 { font-size: 1.4rem; margin-bottom: 15px; color: #222; text-transform: uppercase; font-weight: 800; }
            .program-card p { color: #666; font-size: 1rem; }

            .steps-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; text-align: center; }
            .step-number { font-size: 3rem; font-weight: 900; color: #ff4d4d; margin-bottom: 10px; }
            .step-title { font-size: 1.2rem; font-weight: bold; margin-bottom: 10px; color: #222; }
            .step-text { color: #666; font-size: 0.95rem; }

            .footer { background: #222; color: white; text-align: center; padding: 50px 20px; }
            .footer p { margin-bottom: 10px; font-size: 1.1rem; }
            .footer a { color: #ff4d4d; text-decoration: none; }

            @media (max-width: 768px) {
                .hero h1 { font-size: 3rem; }
                .hero-titles { font-size: 1.1rem; }
                .about-grid { grid-template-columns: 1fr; }
                .steps-grid { grid-template-columns: 1fr 1fr; }
            }
        </style>
    </head>
    <body>

        <!-- 1. ГЛАВНЫЙ ЭКРАН -->
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

        <!-- 2. ОБО МНЕ -->
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

        <!-- 3. ПРОГРАММЫ -->
        <section id="programs" class="section bg-light">
            <div class="container">
                <h2 class="section-title">Выбери <span>программу</span></h2>
                <div class="programs-grid">
                    <div class="program-card">
                        <h3>Снижение и коррекция веса</h3>
                        <p>Составление тренировочной программы с учётом вашего состояния здоровья, физической подготовленности, возраста. Расчёт калорийности вашего рациона и сбалансированного питания.</p>
                    </div>
                    <div class="program-card">
                        <h3>Реабилитация и профилактика проблем с опорно-двигательным аппаратом</h3>
                        <p>Программа тренировок составляется с учётом всех ваших противопоказаний по здоровью.</p>
                    </div>
                    <div class="program-card">
                        <h3>Послеродовое восстановление</h3>
                        <p>Тренировки для восстановления упругости тела.</p>
                    </div>
                    <div class="program-card">
                        <h3>Набор мышечной массы</h3>
                        <p>Программа тренировок и сбалансированное меню.</p>
                    </div>
                    <div class="program-card">
                        <h3>Спортивная подготовка</h3>
                        <p>Если ваша цель — выступления на соревнованиях по фитнесу, составлю план периодизации подготовки к соревнованиям, разработаю питание под разные периоды тренировок.</p>
                    </div>
                    <div class="program-card">
                        <h3>Онлайн-ведение</h3>
                        <p>Тренировки из любой точки мира с полной поддержкой и контролем.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- 4. КАК НАЧАТЬ -->
        <section class="section">
            <div class="container">
                <h2 class="section-title">Как <span>начать</span></h2>
                <div class="steps-grid">
                    <div>
                        <div class="step-number">01</div>
                        <div class="step-title">Выберите программу</div>
                        <div class="step-text">Ознакомьтесь с вариантами и выберите подходящий.</div>
                    </div>
                    <div>
                        <div class="step-number">02</div>
                        <div class="step-title">Выберите дни и часы</div>
                        <div class="step-text">Выберите дни и часы тренировок, которые подходят вам и есть у меня свободные.</div>
                    </div>
                    <div>
                        <div class="step-number">03</div>
                        <div class="step-title">Оплатите</div>
                        <div class="step-text">Оплата помесячная за 8 или 12 тренировок.</div>
                    </div>
                    <div>
                        <div class="step-number">04</div>
                        <div class="step-title">Начинайте тренироваться</div>
                        <div class="step-text">Присоединяйтесь онлайн или оффлайн и начинайте делать фигуру своей мечты.</div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 5. ПОДВАЛ -->
        <footer class="footer">
            <h3 style="color: white; margin-bottom: 20px; font-size: 1.5rem;">Свяжитесь со мной</h3>
            <p>Пишите в Директ Instagram: <a href="https://instagram.com/lavitafit.az" target="_blank">@lavitafit.az</a></p>
            <p>В любое удобное для вас время.</p>
            <p style="margin-top: 30px; font-size: 0.9rem; color: #888;">© 2026 Виктория Зыкова. Персональный тренер.</p>
        </footer>

    </body>
    </html>
    """
    return HttpResponse(html)