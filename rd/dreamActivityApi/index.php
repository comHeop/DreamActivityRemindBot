<?php
// 隐藏报错
error_reporting(0);

// 参数检查
if (empty($_GET['schoolId'])) {
  $on_data = array(
      'data' => array(
          'mail' => '',
          'message' => '缺少参数，schoolId',
      ),
  );
  echo json_encode($on_data);
  exit();
}

$schoolId = $_GET['schoolId'];

// 设置默认返回格式
$on_data = array(
    'error' => false,
    'school' => '',
    'admin' => '',
    'qqGroup' => '',
    'msg' => '',
);

try {
    $conn = new mysqli("localhost", "账号", "密码", "库名");
} catch (PDOException $e) {
    $on_data = array(
        'error' => true,
        'msg' => '数据库连接失败',
    );
}
// 检查学校
$getSchooData = $conn->prepare("SELECT * FROM schoolData WHERE uuid = ?;");
$getSchooData->bind_param("i", $schoolId);
$getSchooData->execute();
$result = $getSchooData->get_result();
$schooData = $result->fetch_assoc();
$getSchooData->close();
// 检查schooId是否存在
if (!$schooData) {
    $on_data = array(
        'error'=> true,
        'msg'=> "无效的schooId",
    );
    $conn->close();
    echo json_encode($on_data);
    exit();
}
// 检查是否被禁止
if ($schooData['ban'] !== 0){
    $on_data = array(
        'error'=> true,
        'msg'=> $schooData["errorMsg"],
    );
}
// 检查是否关闭
if ($schooData['open'] !== 0){
    $on_data = array(
        'error'=> true,
        'msg'=> "活动更新已被禁用",
    );
}
if (!$on_data['error']) {
    // 获取d参数并构造请求
    $d = $schooData['d'];
    $url = 'https://appdmkj.5idream.net/v2/activity/activities';
    $options = array(
        'http' => array(
            'header'  => "Content-Type: application/x-www-form-urlencoded",
            'method'  => 'POST',
            'content' => http_build_query(array('d' => $d)),
        ),
            'ssl' => array(
            'verify_peer'      => false,
            'verify_peer_name' => false,
        ),
    );
    
    $context  = stream_context_create($options);
    $response = file_get_contents($url, false, $context);
    
    if ($response === false) {
        $on_data = array(
            'error' => true,
            'msg' => '到梦空间服务器连接失败',
        );
    }
    
    // 解析返回的JSON数据
    $data = json_decode($response, true);
    
    if ($data['code'] != 100) {
        $on_data = array(
            'error' => true,
            'msg' => 'd参数失效，请重新上传',
        );
    }
}

if ($on_data['error']) {
    $stmt = $conn->prepare("UPDATE schoolData SET ban = ?, errorMsg = ? WHERE uuid = ?");
    $ban = 1;
    $stmt->bind_param('isi', $ban, $on_data['msg'], $schoolId);
    $stmt->execute();
    $stmt->close();
    $conn->close();
    $on_data['admin'] = $schooData['qq'];
    $on_data['qqGroup'] = $schooData['qqGroup'];
    echo json_encode($on_data);
    exit();
}
$details = array();
// 存储信息
foreach ($data['data']['list'] as $activity) {
    // 检查活动是否已经存储
    $getActivityList = $conn->prepare("SELECT * FROM activityData WHERE uuid = ? AND schoolID = ?;");
    $getActivityList->bind_param("ii", $activity['activityId'], $schoolId);
    $getActivityList->execute();
    $result = $getActivityList->get_result();
    $ActivityListData = $result->fetch_assoc();
    $getActivityList->close();
    if (!$ActivityListData) {
        // 写入活动信息
        $stmt = $conn->prepare("INSERT INTO activityData (schoolID, uuid, activitytime, boutique, boutiqueStr, catalog2name, imageUrl, name, status, statusText) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
        $schoolID = $schoolId;
        $uuid = $activity['activityId'];
        $activitytime = $activity['activitytime'];
        $boutique = $activity['boutique'];
        $boutiqueStr = $activity['boutiqueStr'];
        $catalog2name = $activity['catalog2name'];
        $imageUrl = $activity['imageUrl'];
        $name = $activity['name'];
        $status = $activity['status'];
        $statusText = $activity['statusText'];
        $stmt->bind_param("iisissssis", $schoolID, $uuid, $activitytime, $boutique, $boutiqueStr, $catalog2name, $imageUrl, $name, $status, $statusText);
        $stmt->execute();
        $stmt->close();
        $details[] = $activity;
    }
}
$on_data['msg'] = $details;
$on_data['school'] = $schooData['name'];
$on_data['admin'] = $schooData['qq'];
$on_data['qqGroup'] = explode(",",$schooData['qqGroup']);
$conn->close();
echo json_encode($on_data);
exit();
?>
