import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    stages: [
        { duration: '20s', target: 10 },
        { duration: '20s', target: 20 },
        { duration: '20s', target: 30 },
        { duration: '20s', target: 40 },
        { duration: '20s', target: 50 },
        { duration: '10s', target: 0 },
    ],
};

export default () => {
    http.get('http://localhost:5000');
    sleep(1);
}
