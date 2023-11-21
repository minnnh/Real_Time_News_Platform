const client = require('./rpc_client');

async function test() {
    try {
        // invoke 'add'
        const addResponse = await client.add(1, 2);
        console.assert(addResponse === 3, 'add function failed');
        // console.log(addResponse);

        // invoke 'getOneNews'
        const getOneNewsResponse = await client.getOneNews();
        console.assert(getOneNewsResponse !== null, 'getOneNews fail');
        console.log(getOneNewsResponse);

        // invoke 'getNewsSummariesForUser'
        const getNewsSummariesResponse = await client.getNewsSummariesForUser('user_test_eamil_3@test.com', 1);
        console.assert(getNewsSummariesResponse !== null, 'getNewsSummariesForUser fail');
        console.log(getNewsSummariesResponse);

        // invoke 'logNewsClickForUser'
        await client.logNewsClickForUser('user_test_eamil_3@test.com', 'test_news');
        console.log('in logNewsClickForUser');
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call the test function
test();
