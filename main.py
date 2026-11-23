
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Schedule Planner</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f4f6f8; margin: 0; padding: 20px; }
    h1 { text-align: center; color: #333; }
    form { max-width: 700px; margin: 0 auto 20px; display: flex; gap: 8px; flex-wrap: wrap; }
    input, select, button { padding: 8px; font-size: 16px; border: 1px solid #ccc; border-radius: 6px; }
    #task { flex: 1; min-width: 150px; }
    button { background: #2b6cb0; color: white; border: none; cursor: pointer; }
    button:hover { background: #22568c; }
    #week { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; max-width: 1200px; margin: 0 auto; }
    .day { background: white; border-radius: 8px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    .day h2 { font-size: 18px; margin-top: 0; color: #2b6cb0; }
    .item { display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid #eee; }
    .item .time { font-weight: bold; margin-right: 6px; }
    .delete { background: #e53e3e; padding: 2px 8px; font-size: 14px; }
    .empty { color: #999; font-style: italic; }
  </style>
</head>
<body>
  <h1>Weekly Schedule Planner</h1>

  <form id="planner-form">
    <select id="day">
      <option>Monday</option>
      <option>Tuesday</option>
      <option>Wednesday</option>
      <option>Thursday</option>
      <option>Friday</option>
      <option>Saturday</option>
      <option>Sunday</option>
    </select>
    <input type="time" id="time" required>
    <input type="text" id="task" placeholder="What do you need to do?" required>
    <button type="submit">Add</button>
  </form>

  <div id="week"></div>

  <script>
    const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

    // Load saved tasks from the browser, or start empty
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

    function saveTasks() {
      localStorage.setItem("tasks", JSON.stringify(tasks));
    }

    function showSchedule() {
      const week = document.getElementById("week");
      week.innerHTML = "";

      days.forEach(function (day) {
        const box = document.createElement("div");
        box.className = "day";
        box.innerHTML = "<h2>" + day + "</h2>";

        // This day's tasks, sorted by time
        const dayTasks = tasks
          .filter(t => t.day === day)
          .sort((a, b) => a.time.localeCompare(b.time));

        if (dayTasks.length === 0) {
          box.innerHTML += '<p class="empty">Nothing planned</p>';
        }

        dayTasks.forEach(function (t) {
          const row = document.createElement("div");
          row.className = "item";

          const text = document.createElement("span");
          text.innerHTML = '<span class="time">' + t.time + "</span>";
          text.append(t.text);

          const del = document.createElement("button");
          del.className = "delete";
          del.textContent = "X";
          del.onclick = function () {
            tasks = tasks.filter(x => x.id !== t.id);
            saveTasks();
            showSchedule();
          };

          row.append(text, del);
          box.append(row);
        });

        week.append(box);
      });
    }

    document.getElementById("planner-form").addEventListener("submit", function (e) {
      e.preventDefault();
      tasks.push({
        id: Date.now(),
        day: document.getElementById("day").value,
        time: document.getElementById("time").value,
        text: document.getElementById("task").value
      });
      saveTasks();
      showSchedule();
      document.getElementById("task").value = "";
    });

    showSchedule();
  </script>
</body>
</html><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Schedule Planner</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f4f6f8; margin: 0; padding: 20px; }
    h1 { text-align: center; color: #333; }
    form { max-width: 700px; margin: 0 auto 20px; display: flex; gap: 8px; flex-wrap: wrap; }
    input, select, button { padding: 8px; font-size: 16px; border: 1px solid #ccc; border-radius: 6px; }
    #task { flex: 1; min-width: 150px; }
    button { background: #2b6cb0; color: white; border: none; cursor: pointer; }
    button:hover { background: #22568c; }
    #week { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; max-width: 1200px; margin: 0 auto; }
    .day { background: white; border-radius: 8px; padding: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    .day h2 { font-size: 18px; margin-top: 0; color: #2b6cb0; }
    .item { display: flex; justify-content: space-between; align-items: center; padding: 6px 0; border-bottom: 1px solid #eee; }
    .item .time { font-weight: bold; margin-right: 6px; }
    .delete { background: #e53e3e; padding: 2px 8px; font-size: 14px; }
    .empty { color: #999; font-style: italic; }
  </style>
</head>
<body>
  <h1>Weekly Schedule Planner</h1>

  <form id="planner-form">
    <select id="day">
      <option>Monday</option>
      <option>Tuesday</option>
      <option>Wednesday</option>
      <option>Thursday</option>
      <option>Friday</option>
      <option>Saturday</option>
      <option>Sunday</option>
    </select>
    <input type="time" id="time" required>
    <input type="text" id="task" placeholder="What do you need to do?" required>
    <button type="submit">Add</button>
  </form>

  <div id="week"></div>

  <script>
    const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

    // Load saved tasks from the browser, or start empty
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

    function saveTasks() {
      localStorage.setItem("tasks", JSON.stringify(tasks));
    }

    function showSchedule() {
      const week = document.getElementById("week");
      week.innerHTML = "";

      days.forEach(function (day) {
        const box = document.createElement("div");
        box.className = "day";
        box.innerHTML = "<h2>" + day + "</h2>";

        // This day's tasks, sorted by time
        const dayTasks = tasks
          .filter(t => t.day === day)
          .sort((a, b) => a.time.localeCompare(b.time));

        if (dayTasks.length === 0) {
          box.innerHTML += '<p class="empty">Nothing planned</p>';
        }

        dayTasks.forEach(function (t) {
          const row = document.createElement("div");
          row.className = "item";

          const text = document.createElement("span");
          text.innerHTML = '<span class="time">' + t.time + "</span>";
          text.append(t.text);

          const del = document.createElement("button");
          del.className = "delete";
          del.textContent = "X";
          del.onclick = function () {
            tasks = tasks.filter(x => x.id !== t.id);
            saveTasks();
            showSchedule();
          };

          row.append(text, del);
          box.append(row);
        });

        week.append(box);
      });
    }

    document.getElementById("planner-form").addEventListener("submit", function (e) {
      e.preventDefault();
      tasks.push({
        id: Date.now(),
        day: document.getElementById("day").value,
        time: document.getElementById("time").value,
        text: document.getElementById("task").value
      });
      saveTasks();
      showSchedule();
      document.getElementById("task").value = "";
    });

    showSchedule();
  </script>
</body>
</html>
