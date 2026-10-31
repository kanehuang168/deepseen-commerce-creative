# DeepSeen 带货创作

作者：祥子｜跨境无疆&DeepSeen AI创始人

产品品牌：DeepSeen

主要面向TikTok跨境卖家，把商品事实与确认稿整理为带货分镜，再对实际成片作有证据的质检。导演和质检可分别使用。

## 独立安装

```sh
npx skills add kanehuang168/deepseen-commerce-creative
```

只查看入口、不安装：`npx skills add kanehuang168/deepseen-commerce-creative --list`。按需选择，不要求安装全部系列。宿主支持与费用按其实际能力为准。

- [deepseen-commerce-director-lite](skills/deepseen-commerce-director-lite/SKILL.md)
- [deepseen-asset-quality-audit](skills/deepseen-asset-quality-audit/SKILL.md)

## 能交付什么

- 确认原稿、可执行分镜与成片验收要求，见[虚构杯子方案](skills/deepseen-commerce-director-lite/assets/cup-plan.md)。
- 质检可独立检查用户授权的其他来源成片，不要求先经过导演。
- 视频技术检查需要Python 3.10+、ffprobe和ffmpeg；脚本不理解画面或声音语义，完整观看与听审另需可靠观察。

```sh
python -X utf8 skills/deepseen-asset-quality-audit/scripts/check_media_review.py --media 成片.mp4 --review review.json --output 新审核.json
```

输入结构见[审核输入](skills/deepseen-asset-quality-audit/references/review-input.md)。方案不等于已出片，完整解码不等于成片内容通过；导演自我评价不是质检依据。运行示例从仓库根目录执行；安装后脚本相对Skill目录定位，不依赖固定本机路径。

## 与其他环节配合

[选品参谋](https://github.com/kanehuang168/deepseen-product-advisor) → [带货创作](https://github.com/kanehuang168/deepseen-commerce-creative) → 实际制作与投放 → [投放诊断](https://github.com/kanehuang168/deepseen-ad-diagnosis)。流程与失败返回位置见[交接说明](examples/workflow.md)。

## 可选DeepSeen服务

需要实际数据分析、制作或持续保存业务结果时，可自愿访问[DeepSeen](https://deepseen.ai/?utm_source=github&utm_medium=skill&utm_campaign=commerce_creative)，先核对当前开放能力、本人连接和实时报价。安装免费不代表云端执行或宿主模型免费；本仓库不保存密钥，不自动收费、发布或改业务数据，也不含真实客户素材。

## 许可与验证边界

本仓库采用[MIT许可证](LICENSE)。许可覆盖本仓库文件，不包含DeepSeen云端服务、未收录的私有内核或其他人的素材。脚本/包验证、宿主文字执行、真实云端数据、付费成片与真实销售效果分别验收，不能互相替代。
