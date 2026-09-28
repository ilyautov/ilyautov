<a href="https://aifrontier.tech"><img src="assets/hero.svg" width="100%" alt="Ilya Utov, AI Frontier lab: AI tools that do the actual work. 2612 API methods over MCP, 34 skills for small business, no AI inside Cordon."></a>

I build open-source AI tools that do actual work, not demos: agent skills, MCP servers and systems that run inside a company's perimeter. The math runs in code, the data comes from real registries, and it all ships under MIT or Apache 2.0. I run [**AI Frontier**](https://aifrontier.tech), a small lab that puts practical AI into real companies.

<p>
<a href="https://github.com/ilyautov/humanizer-ru"><img src="assets/card-humanizer-ru.svg" width="49%" alt="humanizer-ru: strips the AI tells out of Russian text, scanner included"></a>
<a href="https://github.com/ilyautov/inn-check-ru"><img src="assets/card-inn-check-ru.svg" width="49%" alt="inn-check-ru: one tax ID, a sourced dossier of a Russian company"></a>
</p>
<p>
<a href="https://github.com/ilyautov/cordon"><img src="assets/card-cordon.svg" width="49%" alt="Cordon: your agent reads anything and obeys only you"></a>
<a href="https://github.com/ilyautov/small-business-ru"><img src="assets/card-small-business-ru.svg" width="49%" alt="small-business-ru: 34 skills for Russian small business, numbers computed in code"></a>
</p>

[**humanizer-ru**](https://github.com/ilyautov/humanizer-ru) [![stars](https://img.shields.io/github/stars/ilyautov/humanizer-ru?style=flat-square&label=%E2%98%85&color=555)](https://github.com/ilyautov/humanizer-ru/stargazers) strips the AI fingerprint out of Russian text: bureaucratese, English calques, the tells that give ChatGPT and Claude away. It scores a text from 0 to 100 and shows which phrases gave it away. Try it in the browser at [humanizer-ru.aifrontier.tech](https://humanizer-ru.aifrontier.tech/). Same thing for Italian: [humanizer-it](https://github.com/ilyautov/humanizer-it).

[**inn-check-ru**](https://github.com/ilyautov/inn-check-ru) gives your agent a Russian tax ID and gets back a company dossier: status, finances, debts, court cases, owners and links. Every fact carries its source and date, and whatever could not be checked stays visible. Skill, MCP server and CLI. [inn-check-ru.aifrontier.tech](https://inn-check-ru.aifrontier.tech/)

[**cordon**](https://github.com/ilyautov/cordon) is a prompt-injection firewall with no AI inside. Web pages, emails, issues and tool results can carry orders aimed at your agent; Cordon lets the agent read them and stops it acting on them. Plain code decides, so it cannot be talked round. Adapters for Claude Code, Codex CLI, Gemini CLI, MCP hosts and LangChain. [cordon.aifrontier.tech](https://cordon.aifrontier.tech/en/)

[**small-business-ru**](https://github.com/ilyautov/small-business-ru) is 34 skills for Russian small businesses: taxes, cash, contracts, checking a counterparty. The numbers get computed, not guessed. [small-business-ru.aifrontier.tech](https://small-business-ru.aifrontier.tech/)

<a href="https://github.com/ilyautov/marketplaces-mcp-ru"><img src="assets/mcp.svg" width="100%" alt="MCP servers: 1022 methods for marketplaces, 892 for MoySklad, 698 for business systems"></a>

[**marketplaces-mcp-ru**](https://github.com/ilyautov/marketplaces-mcp-ru) wires Claude or Cursor straight into Wildberries, Ozon, Yandex Market and Avito: sales, orders, stock, prices and finance over the Seller APIs, no browser, no scraping. One marketplace at a time if that is all you need: [ozon](https://github.com/ilyautov/ozon-mcp-ru), [wildberries](https://github.com/ilyautov/wildberries-mcp-ru), [yandex-market](https://github.com/ilyautov/yandex-market-mcp-ru), [avito](https://github.com/ilyautov/avito-mcp-ru).

[**moysklad-mcp-ru**](https://github.com/ilyautov/moysklad-mcp-ru) does the same for MoySklad, the cloud ERP most Russian retail keeps its stock and trade documents in: 892 methods behind 10 generic tools, a safety gate before anything gets written and a draft before anything gets posted.

[**business-mcp-ru**](https://github.com/ilyautov/business-mcp-ru) covers the rest of what a Russian company runs on: [hh.ru](https://github.com/ilyautov/hh-mcp-ru) hiring, [VK](https://github.com/ilyautov/vk-mcp-ru), the legally binding EDI operators [Diadoc](https://github.com/ilyautov/diadoc-mcp-ru) and [SBIS](https://github.com/ilyautov/sbis-mcp-ru), and [Chestny ZNAK](https://github.com/ilyautov/chestny-znak-mcp-ru) product marking. They share one engine, [schema-mcp-core](https://github.com/ilyautov/schema-mcp-core), so a safety fix lands in all of them at once. Method maps, API keys and the errors that eat the most time are written up per service at [business-mcp-ru.aifrontier.tech](https://business-mcp-ru.aifrontier.tech/) and [marketplaces-mcp-ru.aifrontier.tech](https://marketplaces-mcp-ru.aifrontier.tech/).

**Also**

[**hefest**](https://github.com/ilyautov/hefest). Chemical safety for an industrial plant, fully offline: emergency cards, hazard zones, storage compatibility, protective gear. It refuses to answer without grounds, because here an error costs somebody's health.

[**consilium-principis**](https://github.com/ilyautov/consilium-principis). An advisory board of historical thinkers. Every quote is checked word for word against public-domain sources, or the board keeps quiet.

[**doc2md**](https://github.com/ilyautov/doc2md). Batch-converts Word, Excel, PowerPoint, PDF, EPUB, RTF and CSV into clean Markdown before the agent reads them.

[**rusvoice**](https://github.com/ilyautov/rusvoice). Russian voice-over in your own voice, with the layer before synthesis that was missing: stress marks, a brand dictionary, abbreviations read letter by letter.

All of it plugs into Claude Code, Cursor, Codex and other agents. The full list, grouped by what it does, is at [ilyautov.github.io](https://ilyautov.github.io/).

**Star the one you'd actually use.** Then come find me at [aifrontier.tech](https://aifrontier.tech), on [LinkedIn](https://www.linkedin.com/in/ilyautov), or on [Telegram](https://t.me/gorilla_under_hood), where I write up how the whole thing gets built.

<details>
<summary>🇷🇺 По-русски</summary>

<br>

Пишу открытые AI-инструменты, которые делают работу, а не крутят демо: скиллы для агентов, MCP-серверы и системы, которые работают внутри контура предприятия. Считает всё код, данные берутся из настоящих реестров, лицензии MIT и Apache 2.0. Веду лабораторию [**AI Frontier**](https://aifrontier.tech): маленькая команда, которая заводит ИИ в реальные компании.

[**humanizer-ru**](https://github.com/ilyautov/humanizer-ru) вычищает из русского текста следы нейросети: канцелярит, кальки, обороты, по которым сразу видно ChatGPT и Claude. Ставит тексту балл от 0 до 100 и показывает, что его выдало. Попробовать в браузере: [humanizer-ru.aifrontier.tech](https://humanizer-ru.aifrontier.tech/). То же для итальянского: [humanizer-it](https://github.com/ilyautov/humanizer-it).

[**inn-check-ru**](https://github.com/ilyautov/inn-check-ru): даёшь агенту ИНН, получаешь досье компании. Статус, финансы, долги, суды, владельцы и связи, у каждого факта источник и дата, непроверенное видно. Скилл, MCP-сервер и CLI. [inn-check-ru.aifrontier.tech](https://inn-check-ru.aifrontier.tech/)

[**cordon**](https://github.com/ilyautov/cordon): файрвол от промпт-инъекций без ИИ внутри. В письме, на странице или в задаче может сидеть чужая команда для агента. Cordon даёт агенту это прочитать и не даёт выполнить. Решает обычный код, поэтому его не уговоришь. Адаптеры для Claude Code, Codex CLI, Gemini CLI, MCP-хостов и LangChain. [cordon.aifrontier.tech](https://cordon.aifrontier.tech/)

[**small-business-ru**](https://github.com/ilyautov/small-business-ru): 34 скилла для малого бизнеса: налоги, деньги, договоры, проверка контрагента. Цифры считает код, а не выдумывает модель. [small-business-ru.aifrontier.tech](https://small-business-ru.aifrontier.tech/)

[**marketplaces-mcp-ru**](https://github.com/ilyautov/marketplaces-mcp-ru) подключает Claude или Cursor прямо к кабинетам Wildberries, Ozon, Яндекс Маркета и Авито: продажи, заказы, остатки, цены, финансы через Seller API, без браузера и парсинга. Нужен один маркетплейс, ставится один: [ozon](https://github.com/ilyautov/ozon-mcp-ru), [wildberries](https://github.com/ilyautov/wildberries-mcp-ru), [yandex-market](https://github.com/ilyautov/yandex-market-mcp-ru), [avito](https://github.com/ilyautov/avito-mcp-ru).

[**moysklad-mcp-ru**](https://github.com/ilyautov/moysklad-mcp-ru): то же для МойСклада, на котором держится учёт розницы и опта. 892 метода через десять общих инструментов, гейт безопасности перед любой записью и черновик прежде, чем документ будет проведён.

[**business-mcp-ru**](https://github.com/ilyautov/business-mcp-ru): всё остальное, на чём держится российская компания. Наём в [hh.ru](https://github.com/ilyautov/hh-mcp-ru), [VK](https://github.com/ilyautov/vk-mcp-ru), юридически значимое ЭДО [Диадок](https://github.com/ilyautov/diadoc-mcp-ru) и [СБИС](https://github.com/ilyautov/sbis-mcp-ru), маркировка в [Честном знаке](https://github.com/ilyautov/chestny-znak-mcp-ru). Общее ядро [schema-mcp-core](https://github.com/ilyautov/schema-mcp-core): правка безопасности чинит все серверы сразу. Карты методов, где брать ключи и что значат частые ошибки, разобраны на [business-mcp-ru.aifrontier.tech](https://business-mcp-ru.aifrontier.tech/) и [marketplaces-mcp-ru.aifrontier.tech](https://marketplaces-mcp-ru.aifrontier.tech/).

**Ещё**

[**hefest**](https://github.com/ilyautov/hefest). Химическая безопасность завода, целиком офлайн: аварийные карточки, зоны заражения, совместимость хранения, подбор СИЗ. Без оснований не отвечает: ошибка тут стоит здоровья.

[**consilium-principis**](https://github.com/ilyautov/consilium-principis). Совет исторических мыслителей. Каждая цитата сверяется дословно с источником в общественном достоянии, иначе совет молчит.

[**doc2md**](https://github.com/ilyautov/doc2md). Пакетно превращает Word, Excel, PowerPoint, PDF, EPUB, RTF и CSV в чистый Markdown до того, как их прочитает агент.

[**rusvoice**](https://github.com/ilyautov/rusvoice). Русская озвучка своим голосом и слой перед синтезом, которого не хватало: ударения, словарь брендов, аббревиатуры по буквам.

Всё работает с Claude Code, Cursor, Codex и другими агентами. Полный список по назначению: [ilyautov.github.io](https://ilyautov.github.io/).

</details>
