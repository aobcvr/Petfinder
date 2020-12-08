var config = {
    apiKey: "AIzaSyAaf-4vaiqhH8HTRyq4zWkCFoX9x82cdsU",
    authDomain: "web-notifications-c3ca0.firebaseapp.com",
    databaseURL: "https://web-notifications-c3ca0.firebaseio.com",
    projectId: "web-notifications-c3ca0",
    storageBucket: "web-notifications-c3ca0.appspot.com",
    messagingSenderId: "543434318086"
};

firebase.initializeApp(config);


if (window.location.protocol === 'https:' &&
    'Notification' in window &&
    'serviceWorker' in navigator &&
    'localStorage' in window &&
    'fetch' in window &&
    'postMessage' in window
) {
    var messaging = firebase.messaging();
    getToken();
} else {
    if (window.location.protocol !== 'https:') {
        console.error('Is not from HTTPS');
    } else if (!('Notification' in window)) {
        console.error('Notification not supported');
    } else if (!('serviceWorker' in navigator)) {
        console.error('ServiceWorker not supported');
    } else if (!('localStorage' in window)) {
        console.error('LocalStorage not supported');
    } else if (!('fetch' in window)) {
        console.error('fetch not supported');
    } else if (!('postMessage' in window)) {
        console.error('postMessage not supported');
    }

    console.warn('This browser does not support desktop notification.');
    console.log('Is HTTPS', window.location.protocol === 'https:');
    console.log('Support Notification', 'Notification' in window);
    console.log('Support ServiceWorker', 'serviceWorker' in navigator);
    console.log('Support LocalStorage', 'localStorage' in window);
    console.log('Support fetch', 'fetch' in window);
    console.log('Support postMessage', 'postMessage' in window);
}

// Подписываемся
function getToken() {
    // 1. Запрос разрешения у пользователя (всплывающее окно "разрешить/запретить")
    messaging.requestPermission()
        .then(function (permission) {
            console.log('permission', permission);
            // 2.1 Если пользователь разрешил, то получаем токен
            messaging.getToken()
                .then(function (token) {
                    console.log('token', token);
                    fetch('/fcm/register/' + token, {
                        'method': 'POST',
                        'Content-Type': 'application/json'
                    }).then(function (res) {
                        // Если подписка разрешена, то получим объект с данными подписки
                        console.log('/fcm/register/ responsed: ', res);
                    }).catch(function (error) {
                        console.error('Unable to get permission to notify.', error);
                    });
                });
        })
        .catch(function (error) {
            // 2.2 Если пользователь запретил подписку эта функция будет выполняться
            // при каждой загрузке страницы
            console.error('Unable to get permission to notify.', error);
        });
};
