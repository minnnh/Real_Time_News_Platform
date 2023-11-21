var express = require('express');
var rpc_client = require('../rpc_client/rpc_client');
var router = express.Router();

 /* GET one news. */
// router.get('/', function(req, res, next) {
//   console.log('Fetching news...');

//   rpc_client.getOneNews(function(response) {
//     res.json(response);
//   });
// });

 /* GET one news. */
router.get('/', async (req, res, next) => {
  try {
    console.log('Fetching news...');
    
    const news = await rpc_client.getOneNews();
    
    res.json(news);
  } catch (error) {
    console.error('Error fetching news:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

 /* GET news list. */
router.get('/userId/:userId/pageNum/:pageNum', async (req, res, next) => {
  try {
    console.log('Fetching news...');
    const user_id = req.params.userId;
    const page_num = req.params.pageNum;

    const newsSummaries = await rpc_client.getNewsSummariesForUser(user_id, page_num);
    res.json(newsSummaries);
  } catch (error) {
    console.error('Error fetching news:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

/* POST news click event. */
router.post('/userId/:userId/newsId/:newsId', async (req, res, next) => {
  try {
    console.log('Logging news click...');
    const user_id = req.params.userId;
    const news_id = req.params.newsId;

    await rpc_client.logNewsClickForUser(user_id, news_id);
    res.status(200).send('News click logged successfully');
  } catch (error) {
    console.error('Error logging news click:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});
/* POST news click event. */

module.exports = router;



