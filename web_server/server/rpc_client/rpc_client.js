var jayson = require('jayson');
var util = require('util');
//create a client
var client = jayson.client.http({
    hostname: 'localhost',
    port: 4040
});

const clientRequestPromise = util.promisify(client.request.bind(client));

//Test Rpc method
async function add(a, b) {
    try {
        const response = await clientRequestPromise('add', [a, b]);
        return response.result;
    } catch (error) {
        throw error;
    }
}


async function getOneNews() {
    try {
        const response = await clientRequestPromise('getOneNews', []);
        return response.result;
    } catch (error) {
        throw error;
    }
}


async function getNewsSummariesForUser(user_id, page_num) {
    try {
        const response = await clientRequestPromise('getNewsSummariesForUser', [user_id, page_num]);
        return response.result;
    } catch (error) {
        throw error;
    }
}

async function logNewsClickForUser(user_id, news_id) {
    try {
        const response = await clientRequestPromise('logNewsClickForUser', [user_id, news_id]);
        return response.result;
    } catch (error) {
        throw error;
    }
}


module.exports = {
    add: add,
    getOneNews: getOneNews,
    getNewsSummariesForUser: getNewsSummariesForUser,
    logNewsClickForUser: logNewsClickForUser
};
