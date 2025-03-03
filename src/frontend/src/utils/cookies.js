export function setCookie(id, value) {
    document.cookie = id + '=' + value;
}

export function getCookie(id) {
    let value = document.cookie.match('(^|;)?' + id + '=([^;]*)(;|$)');
    return value ? unescape(value[2]) : null;
}

export function deleteCookie(id) {
    document.cookie = id + '=;';
}