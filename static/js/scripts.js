function IncrementCounter() {
            fetch('/increment', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('counter').textContent = data.counter;
                    // console.log(data);
                });
        }

function UpgradeCounter() {
            fetch('/upgrade', { method: 'POST'})
              .then(response => response.json())
              .then(data => {
                document.getElementById('counter').textContent = data.counter;
                document.getElementById('upgrade').textContent = data.click_value;

        if (data.message && data.message.length > 0) {
            alert(data.message[0]);  // メッセージをアラートで表示
        }
      })
}
