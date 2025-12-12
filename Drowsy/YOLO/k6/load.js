import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
    stages: [
        { duration: '30s', target: 100 },
        { duration: '45s', target: 100 },
        { duration: '5s', target: 0 },
    ],
};

export default () => {
    http.get('http://localhost:5000');
    sleep(1);
}
