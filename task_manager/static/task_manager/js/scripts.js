// task_manager/static/task_manager/js/scripts.js
document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll("button");
    buttons.forEach(button => {
        button.addEventListener("mouseover", function() {
            this.style.transform = "scale(1.05)";
        });
        button.addEventListener("mouseout", function() {
            this.style.transform = "scale(1)";
        });
    });
});

$(document).ready(function() {
    // Предполагается, что вы передаёте задачи из вашего представления
    var tasks = [
        {% for task in tasks %}
        {
            title: '{{ task.title }}',
            start: '{{ task.due_date|date:"Y-m-d H:i:s" }}',
            description: '{% if task.completed %}Завершена{% else %}Запланирована{% endif %}',
            color: '{% if task.completed %}#28a745{% else %}#007bff{% endif %}' // Зеленый для завершённых, синий для запланированных
        }{% if not forloop.last %},{% endif %}  // Убедитесь, что не ставится запятая после последнего элемента
        {% endfor %}
    ];

    // Инициализация FullCalendar
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        selectable: true,
        events: tasks, // Передаем события в календарь
        eventRender: function(event, element) {
            // Если вы хотите отображать описание задачи
            element.attr('title', event.description);
        },
        select: function(start, end) {
            $('#due_date').val(start.format('YYYY-MM-DDTHH:mm')); // Установка выбранной даты и времени в поле ввода
            $('#calendar').fullCalendar('unselect'); // Сбрасываем выделение
        }
    });

    // Темная/Светлая тема
    $('#toggle-theme').click(function() {
        $('body').toggleClass('light');
        $('.left-column, .right-column').toggleClass('light');
        $('a').toggleClass('light');
        $('h1, h2').toggleClass('light');
        $('button').toggleClass('light');
    });
});