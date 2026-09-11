### Ilya Utov · Илья Утов

I build open-source AI tools that do actual work, not demos. Agent skills, MCP servers, and one full on-prem system. The math runs in code, the data comes from real registries, and it all ships under MIT or Apache 2.0.

I run [**AI Frontier**](https://aifrontier.tech), a small lab that puts practical AI into real companies.

**Skills for agents**

[**humanizer-ru**](https://github.com/ilyautov/humanizer-ru) [![stars](https://img.shields.io/github/stars/ilyautov/humanizer-ru?style=flat-square&label=%E2%98%85&color=555)](https://github.com/ilyautov/humanizer-ru/stargazers) Strips the AI fingerprint out of Russian text: bureaucratese, English calques, the tells that give ChatGPT and Claude away. This README went through it.

[**consilium-principis**](https://github.com/ilyautov/consilium-principis). An advisory board of historical thinkers. Every quote is checked word for word against public-domain sources, or the board keeps quiet. Fail-closed, no paraphrase passed off as a citation.

[**small-business-ru**](https://github.com/ilyautov/small-business-ru). 34 skills for Russian small businesses: taxes, cash, checking a counterparty by its tax ID. The numbers get computed, not guessed.

[**humanizer-it**](https://github.com/ilyautov/humanizer-it). Same as humanizer-ru, for Italian.

**Bridges into real systems (MCP)**

[**marketplaces-mcp-ru**](https://github.com/ilyautov/marketplaces-mcp-ru). Wires Claude or Cursor straight into Wildberries, Ozon, Yandex Market and Avito: sales, orders, stock, prices, finance over the Seller APIs. 1022 methods, no browser, no scraping. One marketplace at a time if that is all you need: [ozon-mcp-ru](https://github.com/ilyautov/ozon-mcp-ru), [wildberries-mcp-ru](https://github.com/ilyautov/wildberries-mcp-ru), [yandex-market-mcp-ru](https://github.com/ilyautov/yandex-market-mcp-ru), [avito-mcp-ru](https://github.com/ilyautov/avito-mcp-ru).

[**business-mcp-ru**](https://github.com/ilyautov/business-mcp-ru). Five more servers for the systems a Russian company actually runs on: [hh.ru](https://github.com/ilyautov/hh-mcp-ru) hiring, [VK](https://github.com/ilyautov/vk-mcp-ru), the two legally binding EDI operators [Diadoc](https://github.com/ilyautov/diadoc-mcp-ru) and [SBIS](https://github.com/ilyautov/sbis-mcp-ru), and [Chestny ZNAK](https://github.com/ilyautov/chestny-znak-mcp-ru) product marking. 698 methods, one shared engine in [schema-mcp-core](https://github.com/ilyautov/schema-mcp-core), so a safety fix lands in all of them at once.

[**moysklad-mcp-ru**](https://github.com/ilyautov/moysklad-mcp-ru). The same for MoySklad: stock, orders, documents, reports, with a safety gate before anything gets written.

**Systems**

[**hefest**](https://github.com/ilyautov/hefest). Chemical safety for an industrial plant, fully offline: emergency cards, hazard zones, storage compatibility, protective gear. It refuses to answer without grounds and never converts units on its own. The cost of an error here is somebody's health, so silence beats a plausible guess.

[**cordon**](https://github.com/ilyautov/cordon). A deterministic layer between untrusted content and agent actions: it removes the hidden layer, remembers where data came from, and keeps calls inside the boundaries of the intent.

[**doc2md**](https://github.com/ilyautov/doc2md). Batch-converts Word, Excel, PowerPoint, PDF, EPUB, RTF and CSV into clean Markdown before the agent reads them, so the model spends its context on the content and not on the file format.

[**rusvoice**](https://github.com/ilyautov/rusvoice). Russian voice-over in your own voice. Cloning is solved by open code; what was missing is the layer before synthesis: stress marks, a brand dictionary, abbreviations read letter by letter, and a way to see what the pipeline will do to a line before you hear it.

All of it plugs into Claude Code, Cursor, Codex and other agents. The method maps, the API keys and the errors that eat the most time are written up per service at [business-mcp-ru.aifrontier.tech](https://business-mcp-ru.aifrontier.tech/) and [marketplaces-mcp-ru.aifrontier.tech](https://marketplaces-mcp-ru.aifrontier.tech/), built from the same catalogs the servers execute.

Everything above sits in one list at [ilyautov.github.io](https://ilyautov.github.io/), grouped by what it does, if you'd rather scan it at a glance than scroll the repo tab.

**Star the one you'd actually use.** Then come find me at [aifrontier.tech](https://aifrontier.tech), on [LinkedIn](https://www.linkedin.com/in/ilyautov), or on [Telegram](https://t.me/gorilla_under_hood), where I write up how the whole thing gets built.

<details>
<summary>🇷🇺 По-русски</summary>

<br>

Пишу открытые AI-инструменты, которые делают работу, а не крутят демо. Скиллы для агентов, MCP-серверы и одна цельная система, работающая внутри контура предприятия. Считает всё код, данные берутся из настоящих реестров, лицензии MIT и Apache 2.0.

Веду лабораторию [**AI Frontier**](https://aifrontier.tech): маленькая команда, которая заводит ИИ в реальные компании.

**Скиллы для агентов**

[**humanizer-ru**](https://github.com/ilyautov/humanizer-ru) [![звёзды](https://img.shields.io/github/stars/ilyautov/humanizer-ru?style=flat-square&label=%E2%98%85&color=555)](https://github.com/ilyautov/humanizer-ru/stargazers) Вычищает из русского текста следы нейросети: канцелярит, кальки, обороты, по которым сразу видно ChatGPT и Claude. Этим скиллом причёсан и сам текст, который вы читаете.

[**consilium-principis**](https://github.com/ilyautov/consilium-principis). Совет исторических мыслителей. Каждая цитата сверяется дословно с источником в общественном достоянии, иначе совет молчит. Пересказ, выданный за цитату, не пройдёт.

[**small-business-ru**](https://github.com/ilyautov/small-business-ru). 34 скилла для малого бизнеса: налоги, деньги, проверка контрагента по ИНН. Цифры считает код, а не выдумывает модель.

[**humanizer-it**](https://github.com/ilyautov/humanizer-it). То же, что humanizer-ru, только для итальянского.

**Мосты к рабочим системам (MCP)**

[**marketplaces-mcp-ru**](https://github.com/ilyautov/marketplaces-mcp-ru). Подключает Claude или Cursor прямо к кабинетам Wildberries, Ozon, Яндекс Маркета и Авито: продажи, заказы, остатки, цены, финансы через Seller API. 1022 метода, без браузера и парсинга. Нужен один маркетплейс, ставится один: [ozon-mcp-ru](https://github.com/ilyautov/ozon-mcp-ru), [wildberries-mcp-ru](https://github.com/ilyautov/wildberries-mcp-ru), [yandex-market-mcp-ru](https://github.com/ilyautov/yandex-market-mcp-ru), [avito-mcp-ru](https://github.com/ilyautov/avito-mcp-ru).

[**business-mcp-ru**](https://github.com/ilyautov/business-mcp-ru). Ещё пять серверов под то, на чём держится российская компания: наём в [hh.ru](https://github.com/ilyautov/hh-mcp-ru), [VK](https://github.com/ilyautov/vk-mcp-ru), два оператора юридически значимого ЭДО [Диадок](https://github.com/ilyautov/diadoc-mcp-ru) и [СБИС](https://github.com/ilyautov/sbis-mcp-ru), маркировка в [Честном знаке](https://github.com/ilyautov/chestny-znak-mcp-ru). 698 методов и общее ядро [schema-mcp-core](https://github.com/ilyautov/schema-mcp-core): правка безопасности чинит все сразу.

[**moysklad-mcp-ru**](https://github.com/ilyautov/moysklad-mcp-ru). То же для МойСклада: остатки, заказы, документы, отчёты, с гейтом безопасности перед любой записью.

**Системы**

[**hefest**](https://github.com/ilyautov/hefest). Химическая безопасность завода, целиком офлайн: аварийные карточки, зоны заражения, совместимость хранения, подбор СИЗ. Отказывается отвечать без оснований и не пересчитывает единицы за человека. Ошибка тут стоит здоровья, поэтому молчание лучше правдоподобной догадки.

[**cordon**](https://github.com/ilyautov/cordon). Детерминированная прослойка между недоверенным содержимым и действиями агента: снимает скрытый слой, помнит, откуда пришли данные, и держит вызовы в границах намерения.

[**doc2md**](https://github.com/ilyautov/doc2md). Пакетно превращает Word, Excel, PowerPoint, PDF, EPUB, RTF и CSV в чистый Markdown до того, как их прочитает агент: контекст уходит на содержание, а не на формат файла.

[**rusvoice**](https://github.com/ilyautov/rusvoice). Русская озвучка своим голосом. Клонировать голос умеет открытый код, дефицитен слой перед синтезом: ударения, словарь брендов, аббревиатуры по буквам и возможность увидеть, что тракт сделает с репликой, до того как её услышишь.

Всё дружит с Claude Code, Cursor, Codex и другими агентами. Карты методов, где брать ключи и что значат частые ошибки, разобраны по сервисам на [business-mcp-ru.aifrontier.tech](https://business-mcp-ru.aifrontier.tech/) и [marketplaces-mcp-ru.aifrontier.tech](https://marketplaces-mcp-ru.aifrontier.tech/): страницы собраны из тех же каталогов, которые исполняет сервер.

Всё перечисленное лежит одним списком на [ilyautov.github.io](https://ilyautov.github.io/), разбито по назначению: так быстрее просмотреть разом, чем листать вкладку репозиториев.

**Поставь звезду тому, чем реально будешь пользоваться.** А если интересно, как это всё собирается, я пишу об этом в [телеграме](https://t.me/gorilla_under_hood) и на [aifrontier.tech](https://aifrontier.tech). Ещё есть [LinkedIn](https://www.linkedin.com/in/ilyautov).

</details>
