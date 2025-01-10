# Eaquira

A python 3 project to send game playlog to「舞萌DX」.
###### dev of SDGA was suspended
---

## Info

__Eaquira__ is a fork of `sdgb-some-api` main branch. Thanks to leakers.

The whole project was powered by Python 3, same as the origin. EVIL Python XD

## SDGA Usage

still in progress...

## SDGB Usage

- _authlite.py_ Get latest opt file of SDGB.
- _login.py_ ```UserLoginApi```
- _logout.py_ ```UserLogoutApi```
- _mapstock.py_ 区域前进保存 99 千米
- _music.py_ 传分
- _preview.py_ ```GetUserPreviewApi```
- _sdgb.py_ 网络发包
- _ticket.py_ ```UpsertUserChargelogApi```
- *unlock_all.py* 解锁「舞萌DX」至「舞萌DX 2024」所有的乐曲，含有 Re:Master 难度的乐曲的 Re:Master 铺面暂无法解锁
- _unlock.py_ 解锁指定歌曲
- _userdata.py_ ```GetUserDataApi```

其中，_mapstock.py_ _music.py_ _ticket.py_ _unlock.py_ _userdata.py_ 均包含完整登录流程，其中 _mapstock.py_ _music.py_ _unlock.py_ 会按照 _settings.py_ 中记录的歌曲信息覆盖原有成绩。

- _settings.py_ 储存 UserId、机厅信息等重要的信息，**请不要向他人泄露自己的 UserId**。将 ```.settings.py``` 命名为 ```settings.py``` 并按照注释修改设置。

## Running

```bash
pip install -r requirements.txt
```

## Warning and Statements

WE ARE NOT RESIPONSIBLE FOR YOUR ACCOUNT.

>怂别用，用别怂。
>
>我也没说过这玩意一直能用，至少现在能用。

## Copyright

GNU License.

__Eaquira__ is a part of [__Project Fragrance__](https://fragrance.moe). 
