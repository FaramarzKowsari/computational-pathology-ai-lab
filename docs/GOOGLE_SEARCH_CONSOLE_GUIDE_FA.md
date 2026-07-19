# راهنمای اتصال Computational Pathology AI Lab به Google Search Console

## آدرس رسمی سایت

https://faramarzkowsari.github.io/computational-pathology-ai-lab/

## نوع Property مناسب

در Google Search Console یک **URL-prefix property** با همین آدرس کامل بسازید:

`https://faramarzkowsari.github.io/computational-pathology-ai-lab/`

از Domain property برای `github.io` استفاده نکنید، چون کنترل DNS دامنهٔ اصلی `github.io` در اختیار GitHub است.

## روش پیشنهادی تأیید مالکیت: HTML file

1. وارد Google Search Console شوید.
2. گزینهٔ **Add property** را انتخاب کنید.
3. در ستون **URL prefix** آدرس زیر را دقیقاً وارد کنید:

   `https://faramarzkowsari.github.io/computational-pathology-ai-lab/`

4. روش **HTML file** را انتخاب کنید.
5. فایل اختصاصی گوگل با نامی شبیه زیر را دانلود کنید:

   `google1234567890abcdef.html`

6. فایل را بدون تغییر نام و بدون تغییر محتوا داخل این مسیر محلی قرار دهید:

   `website/google1234567890abcdef.html`

7. در GitHub Desktop آن را Commit و Push کنید.
8. منتظر سبزشدن Workflow **Deploy GitHub Pages** بمانید.
9. فایل را در مرورگر باز کنید:

   `https://faramarzkowsari.github.io/computational-pathology-ai-lab/google1234567890abcdef.html`

10. وقتی فایل بدون ورود به حساب باز شد، در Search Console روی **Verify** کلیک کنید.
11. فایل تأیید را بعداً حذف نکنید؛ حذف آن می‌تواند تأیید مالکیت را از بین ببرد.

## ارسال Sitemap

پس از تأیید:

1. از منوی سمت چپ وارد **Sitemaps** شوید.
2. در کادر Add a new sitemap فقط این عبارت را وارد کنید:

   `sitemap.xml`

3. روی **Submit** کلیک کنید.

آدرس کامل Sitemap:

`https://faramarzkowsari.github.io/computational-pathology-ai-lab/sitemap.xml`

## بررسی robots.txt

آدرس robots.txt:

`https://faramarzkowsari.github.io/computational-pathology-ai-lab/robots.txt`

محتوای آن باید اجازهٔ Crawl تمام سایت را بدهد و به Sitemap اشاره کند.

## درخواست ایندکس دستی

با ابزار **URL Inspection** این URLها را جداگانه بررسی و سپس **Request Indexing** کنید:

1. `https://faramarzkowsari.github.io/computational-pathology-ai-lab/`
2. `https://faramarzkowsari.github.io/computational-pathology-ai-lab/book.html`
3. `https://faramarzkowsari.github.io/computational-pathology-ai-lab/assets/computational-pathology-engineering.pdf`

## بررسی فایل‌ها پیش از درخواست ایندکس

این URLها باید در حالت Incognito باز شوند:

- `https://faramarzkowsari.github.io/computational-pathology-ai-lab/`
- `https://faramarzkowsari.github.io/computational-pathology-ai-lab/book.html`
- `https://faramarzkowsari.github.io/computational-pathology-ai-lab/robots.txt`
- `https://faramarzkowsari.github.io/computational-pathology-ai-lab/sitemap.xml`
- `https://faramarzkowsari.github.io/computational-pathology-ai-lab/assets/computational-pathology-engineering.pdf`
- فایل اختصاصی تأیید گوگل

## Structured Data

صفحهٔ اصلی دارای ساختارهای زیر است:

- Person
- WebPage
- WebSite
- SoftwareSourceCode
- Book

صفحهٔ کتاب نیز دارای:

- Person
- WebPage
- Book
- SoftwareSourceCode relationship

صفحات را با Rich Results Test و Schema Markup Validator بررسی کنید. وجود Schema به‌تنهایی نمایش نتیجهٔ غنی یا Knowledge Panel را تضمین نمی‌کند.

## نکات مهم

- Sitemap فقط یک سیگنال و راهنمای کشف URL است و ایندکس‌شدن را تضمین نمی‌کند.
- robots.txt برای مدیریت Crawl است، نه برای اجرای noindex.
- صفحات اصلی باید canonical خودارجاع داشته باشند.
- صفحهٔ 404 باید `noindex,follow` باشد.
- فایل HTML تأیید Search Console را حذف نکنید.
- پس از هر تغییر مهم، ابتدا Deploy را بررسی و سپس از URL Inspection درخواست Crawl مجدد کنید.
- زمان Crawl و Index ممکن است از چند روز تا چند هفته متغیر باشد.

## پیام Commit پیشنهادی

Summary:

`Add Search Console sitemap robots and SEO pages`

Description:

`Add production robots.txt, XML sitemap, enhanced book metadata, noindex 404 page, and Google Search Console verification guidance for the GitHub Pages deployment.`
