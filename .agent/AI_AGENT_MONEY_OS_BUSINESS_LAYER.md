# AI Agent Money OS — Business Layer

> Hệ thống kinh doanh tự động hoàn chỉnh: 5 business agents, 18 core business skills, 12 marketing skills, 18 commands, 5 workflows.
>
> Phát triển bởi **Vương Duy Định**.

## How This Kit Works

When a user types a `/command`, you:
1. Read the matching command file in `commands/`
2. Activate the assigned Agent (system prompt in `agents/`)
3. Load the relevant Skill (`skills/*/SKILL.md` + `references/` + `templates/`)
4. Follow the Workflow if applicable (`workflows/`)
5. Deliver the output

## Agents

| Agent | File | Core Skills | Marketing Skills |
|-------|------|-------------|-------------|
| **Offer Agent** | `agents/01-offer-agent.md` | market-research, competitor-analysis, offer-packaging | offer-architect, money-model |
| **Attraction Agent** | `agents/02-attraction-agent.md` | funnel-architecture, content-creation, lead-magnet-builder | funnel-strategist, hvco-creator |
| **Conversion Agent** | `agents/03-conversion-agent.md` | sales-page-blueprint, copywriting, objection-handler | ad-copy-machine, vsl-scriptwriter, sales-call-script |
| **Deliver Agent** | `agents/04-deliver-agent.md` | payment-setup-guide, notification-setup-guide, delivery-setup-guide, landing-page-builder, vercel-deployment, payment-embed | — |
| **Insights Agent** | `agents/05-insights-agent.md` | social-analytics, revenue-report, optimization-advisor | — |

## Marketing Skills — 12 Kỹ Năng Bán Hàng

Pipeline marketing tuần tự từ hiểu khách hàng → chốt đơn:

| # | Folder | Tên Tiếng Việt | Chạy Sau | Chạy Trước |
|---|--------|----------------|----------|------------|
| 01 | `avatar-builder` | **Xây Dựng Chân Dung Khách Hàng** | — | Tất cả |
| 02 | `brand-voice` | **Xây Dựng Giọng Nói Thương Hiệu** | 01 | 08-12 |
| 03 | `hero-mechanism` | **Xây Dựng USP** | 01 | 04, 05 |
| 04 | `money-model` | **Thiết Kế Money Model** | 03 | 05 |
| 05 | `offer-architect` | **Xây Dựng Offer Không Thể Chối Từ** | 04 | 06, 07 |
| 06 | `hvco-creator` | **Tạo Nội Dung Giá Trị Cao** | 01, 05 | 07, 08 |
| 07 | `funnel-strategist` | **Thiết Kế Blueprint Phễu Bán Hàng** | 04, 05 | 08, 09 |
| 08 | `ad-copy-machine` | **Máy Viết Copy Quảng Cáo** | 07 | 09 |
| 09 | `vsl-scriptwriter` | **Viết Kịch Bản Video Bán Hàng** | 08 | — |
| 10 | `email-closer` | **Viết Email Bán Hàng Tự Động** | 07 | 11 |
| 11 | `follow-up-engine` | **Hệ Thống Follow-up** | 10 | — |
| 12 | `sales-call-script` | **Kịch Bản Gọi Điện Bán Hàng** | 07 | — |

## Commands

### Offer Agent
- `/research [niche]` — Nghiên cứu thị trường
- `/competitor [name]` — Phân tích đối thủ
- `/offer [product]` — Đóng gói offer

### Attraction Agent
- `/funnel [type]` — Thiết kế phễu bán hàng
- `/content [platform] [type]` — Sáng tạo nội dung
- `/lead-magnet [type] [topic]` — Tạo lead magnet

### Conversion Agent
- `/sales-page [action] [product]` — Blueprint trang bán hàng
- `/copy [framework] [context]` — Viết copy thuyết phục
- `/objection [category] [product]` — Xử lý từ chối

### Deliver Agent
- `/payment-setup [step]` — Cài đặt thanh toán SePay VietQR
- `/notification [step]` — Cài đặt Telegram bot
- `/delivery [method]` — Tự động giao hàng số
- `/landing-page [product-type] [style]` — Tạo landing page HTML
- `/deploy [method]` — Deploy lên Vercel
- `/payment-embed [pattern]` — Nhúng thanh toán VietQR

### Insights Agent
- `/analytics [platform] [period]` — Phân tích mạng xã hội
- `/revenue [period]` — Báo cáo doanh thu
- `/optimize [area]` — Tối ưu hiệu suất

## Skills

Each skill lives in `skills/{skill-name}/` with:
- `SKILL.md` — Main skill instructions and methodology
- `references/` — Frameworks, guides, and knowledge bases
- `templates/` — Ready-to-use fill-in templates (where applicable)

## Workflows

| Workflow | File | Duration |
|----------|------|----------|
| Nghiên Cứu & Offer | `workflows/offer-research-workflow.md` | 1-2 ngày |
| Thu Hút & Nội Dung | `workflows/attraction-content-workflow.md` | 3-5 ngày |
| Chuyển Đổi & Bán Hàng | `workflows/conversion-sales-workflow.md` | 2-3 ngày |
| Giao Hàng Tự Động | `workflows/delivery-automation-workflow.md` | 1-2 ngày |
| Insights & Báo Cáo | `workflows/insights-reporting-workflow.md` | Hàng tuần 1-2h |

## Rules

- Address users as "anh/chị" (Vietnamese business courtesy)
- All output content in Vietnamese unless user requests otherwise
- Use Vietnamese examples and VND pricing when relevant
- Tech stack: SePay (payments), Telegram (notifications), FB/IG/TikTok/YouTube/Zalo (content)
- When user asks something ambiguous, map to the closest command and confirm before executing

## Command Execution

When a user types a slash command:

1. **Read** the command file: `commands/{command-name}.md`
2. **Load** the agent system prompt: `agents/{agent-file}.md`
3. **Read** the skill file: `skills/{skill-name}/SKILL.md`
4. **Read** relevant references from: `skills/{skill-name}/references/`
5. **Use** templates if available: `skills/{skill-name}/templates/`
6. **Follow** the workflow if doing end-to-end: `workflows/{workflow-file}.md`
7. **Output** the result in the format specified by the skill

If the user doesn't use a slash command, infer their intent and suggest the right command.

---

*AI Agent Money OS © Vương Duy Định*
