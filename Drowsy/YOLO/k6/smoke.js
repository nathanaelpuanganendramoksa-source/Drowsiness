import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    vus: 1,
    duration: '10s',
};

export default () => {
    let res = http.get('http://localhost:5000');

    check(res, {
        "server returns status 200": (r) => r.status === 200,
    });

    sleep(1);
}
