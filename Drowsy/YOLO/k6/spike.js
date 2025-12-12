import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    stages: [
        { duration: '5s', target: 5 },
        { duration: '1s', target: 200 },
        { duration: '30s', target: 200 },
        { duration: '10s', target: 0 },
    ],
    thresholds: {
        http_req_failed: ['rate<0.05'],
        http_req_duration: ['p(95)<200'],
    },
};

export default () => {
    http.get('http://localhost:5000');
    sleep(1);
}
