# Django_project
# Урок 19.2

## Задание 1

Для начала работы над задачей выполните первые шаги:
Настройте виртуальное окружение.
Создайте новый Django-проект.

## Задание 2

После успешного создания проекта сделайте первую настройку. Для этого:
Создайте первое приложение с названием catalog.
Внесите начальные настройки проекта.
Сделайте настройку урлов (URL-файлов) для нового приложения.

## Задание 3

Подготовьте два шаблона для домашней страницы и страницы с контактной информацией.
Для создания шаблонов лучше использовать UIkit Bootstrap. Это удобный набор элементов, которые уже стилизованы и готовы к использованию. UIkit Bootstrap помогает избежать самостоятельной верстки макетов.

## Задание 4

В приложении в контроллере реализуйте два контроллера:
Контроллер, который отвечает за отображение домашней страницы.
Контроллер, который отвечает за отображение контактной информации.

## * Дополнительное задание

Реализуйте обработку сбора обратной связи от пользователя, который зашел на страницу контактов и отправил свои данные для обратной связи.

# Работа с ORM в Django
# Урок 20.1

## Задание 1

Подключите СУБД PostgreSQL для работы в проекте. Для этого:
Создайте базу данных в ручном режиме.
Внесите изменения в настройки подключения.

## Задание 2

В приложении каталога создайте модели:
Product,
Category.
Опишите для них начальные настройки.

## Задание 3

Для каждой модели опишите следующие поля:
Product:
наименование,
описание,
изображение (превью),
категория,
цена за покупку,
дата создания,
дата последнего изменения.
Category:
наименование,
описание.
Для поля с изображением необходимо добавить соответствующие настройки в проект, а также установить библиотеку для работы с изображениями Pillow.

## Задание 4

Перенесите отображение моделей в базу данных с помощью инструмента миграций. Для этого:
Создайте миграции для новых моделей.
Примените миграции.
Внесите изменения в модель категорий, добавьте поле created_at, примените обновление структуры с помощью миграций.
Откатите миграцию до состояния, когда поле created_at для модели категории еще не существовало, и удалите лишнюю миграцию.

## Задание 5

Для моделей категории и продукта настройте отображение в административной панели. Для категорий выведите id и наименование в список отображения, а для продуктов выведите в список id, название, цену и категорию.
При этом интерфейс вывода продуктов настройте так, чтобы можно было результат отображения фильтровать по категории, а также осуществлять поиск по названию и полю описания.

## Задание 6

Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры. В качестве решения приложите скриншот.
Сформируйте фикстуры для заполнения базы данных.
Напишите кастомную команду, которая умеет заполнять данные в базу данных, при этом предварительно зачищать ее от старых данных.
Последний пункт можно реализовать в связке с инструментом работы с фикстурами, можно описать вставку данных отдельными запросами.

## * Дополнительное задание

В контроллер отображения главной страницы добавьте выборку последних 5 товаров и вывод их в консоль.
Создайте модель для хранения контактных данных и попробуйте вывести данные, заполненные через админку, на страницу с контактами.

# Шаблонизация
# Урок 20.2

## Задание 1
Создайте новый контроллер и шаблон, которые будут отвечать за отображение отдельной страницы с товаром. На странице с товаром необходимо вывести всю информацию о товаре.
Для создания шаблонов используйте UI kit Bootstrap. При возникновении проблем возьмите за основу данный шаблон.

## Задание 2
В созданный ранее шаблон для главной страницы выведите список товаров в цикле. Для единообразия выводимых карточек отображаемое описание обрежьте после первых выведенных 100 символов.

## Задание 3
Из-за расширения количества шаблонов появляется слишком много повторяющегося кода, поэтому выделите общий (базовый) шаблон и также подшаблон с главным меню. При необходимости можно выделить больше общих шаблонов.

## Задание 4
Для выводимого изображения на странице реализуйте шаблонный фильтр, который преобразует переданный путь в полный путь для доступа к медиафайлу:

<!-- Исходный вариант --> 
<img src="/media/{{ object.image }}" />
<!-- Итоговый вариант -->
<img src="{{ object.image|mediapath }}" />

Реализуйте описанный функционал с помощью шаблонного тега:

<!-- Исходный вариант -->
<img src="/media/{{ object.image }}" />
<!-- Итоговый вариант -->
<img src="{% mediapath object.image %}" />

## * Дополнительное задание
Добавьте функционал создания продукта через внешний интерфейс, не используя стандартную админку.
Реализуйте постраничный вывод списка продуктов.

# Урок 21.1 FBV и CBV
## Задание 1
Продолжаем работать с проектом из предыдущего домашнего задания. Переведите имеющиеся контроллеры с FBV на CBV.

## Задание 2
Создайте новую модель блоговой записи со следующими полями:
заголовок,
slug (реализовать через CharField),
содержимое,
превью (изображение),
дата создания,
признак публикации,
количество просмотров.
Для работы с блогом реализуйте CRUD для новой модели.

Slug — человекопонятный URL, представляет собой набор символов, которые можно прочитать как связные слова или предложения в адресной строке, служит уникальным идентификатором записи в рамках одной модели и состоит из безопасных для обработки запроса символов:

0-9
,
a-z
 (обычно в нижнем регистре),
символ 
-
.

## Задание 3
Модифицируйте вывод и обработку запросов, добавив следующую логику на уровне контроллеров:
при открытии отдельной статьи увеличивать счетчик просмотров;
выводить в список статей только те, которые имеют положительный признак публикации;
при создании динамически формировать slug name для заголовка;
после успешного редактирования записи необходимо перенаправлять пользователя на просмотр этой статьи.

## * Дополнительное задание
Когда статья достигает 100 просмотров, отправлять себе на почту поздравление с достижением.
Примечание: для отправки писем рекомендуем использовать почтовый сервис Яндекс.


# Урок 22.1 Формы

## Задание 1

Продолжаем работать с проектом из предыдущего домашнего задания. Для модели продуктов реализуйте механизм CRUD, задействовав модуль 
django.forms.

Условия для пользователей:
могут создавать новые продукты;
не могут загружать запрещенные продукты на платформу.
Для исключения загрузки запрещенных продуктов реализуйте валидацию названия и описания продукта таким образом, чтобы нельзя было в них добавлять слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.

## Задание 2

Добавьте новую модель «Версия», которая должна содержать следующие поля:
продукт,
номер версии,
название версии,
признак текущей версии.
При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.

## Задание 3

Для работы с версиями продукта добавьте реализацию работы с формами. При этом версия может быть внесена только в существующий продукт.

Все созданные формы нужно стилизовать так, чтобы они были в единой стилистике оформления всей платформы. Для этого можно воспользоваться методом 
__init__  либо самостоятельно изучить пакет crispy-forms: https://pypi.org/project/django-crispy-forms/.

## * Дополнительное задание
В один момент времени может быть только одна активная версия продукта, поэтому при изменении версий необходимо проверять, что пользователь в качестве активной версии указал только одну. В случае возникновения ошибки вернуть сообщение пользователю и попросить выбрать только одну активную версию.
