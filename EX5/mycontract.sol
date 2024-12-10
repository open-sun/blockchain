pragma solidity >=0.4.16 <0.9.0;

contract BlockchainSplitwise {
    struct debt{
        uint32 value;//债务
    }
    mapping(address=>mapping(address=>debt)) internal debt_map;//债务图
    function lookup(address debtor, address creditor) public view returns (uint32 ret)//查找
    {
        ret=debt_map[debtor][creditor].value;
    }
    function add_IOU(address creditor, uint32 amount, address[] memory path, uint32 min_path) public {//债权人，新增债务，path，path中用以消除债务的值
    require(amount > 0, "Amount must >0");
    address debtor = msg.sender;  
    require(debtor != creditor, "Creditor cannot = debtor.");
    
    debt storage mydebt =debt_map[debtor][creditor];
    if(min_path==0){
        mydebt.value+=amount;
        return;
    } 
    require((mydebt.value+amount) >= min_path, "min_path need to be the smallest");
    require(creditor == path[0] && debtor == path[path.length - 1], "The path is wrong!");
    for(uint256 i = 0; i < path.length - 1; i++)
        {
            debt storage currentDebt = debt_map[path[i]][path[i + 1]];
            require(currentDebt.value != 0, "debt is 0");
            require(currentDebt.value >= min_path, "min_ptah is bigger than this debt");
            currentDebt.value -= min_path;
        }

        mydebt.value += amount - min_path;
}
}
