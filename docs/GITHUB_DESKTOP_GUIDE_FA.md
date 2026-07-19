# راهنمای فارسی انتقال پروژه با GitHub Desktop

## پیش از شروع

از پوشهٔ فعلی مخزن یک کپی پشتیبان بگیرید. فایل ZIP را در پوشه‌ای جداگانه Extract کنید.

## انتقال فایل‌ها

1. در GitHub Desktop مخزن فعلی `Deep-Learning-Cancer-Detection-CU-Boulder` را باز کنید.
2. از منوی **Repository > Show in Explorer** پوشهٔ محلی مخزن را باز کنید.
3. تمام محتویات پوشهٔ استخراج‌شدهٔ `computational-pathology-ai-lab` را داخل پوشهٔ محلی مخزن کپی کنید.
4. برای فایل‌های همنام گزینهٔ **Replace** را بزنید. فایل‌های قدیمی نوت‌بوک و نتایج حذف نمی‌شوند.
5. روی `PREPARE_WINDOWS.bat` دوبار کلیک کنید. این فایل، نوت‌بوک‌های اصلی، `submission.csv` و تصویر لیدربورد را بدون تغییر به پوشهٔ Legacy منتقل می‌کند و Checksum می‌سازد.
6. پوشهٔ زیر را بررسی کنید:
   `legacy/cu_boulder_original_assignment/`
7. در GitHub Desktop همهٔ تغییرات را مرور کنید. دادهٔ خصوصی، کلید API، فایل `.env` یا وزن مدل را Commit نکنید.
8. Summary پیشنهادی:
   `Transform project into Computational Pathology AI Lab v1.0.0`
9. روی **Commit to main** و سپس **Push origin** بزنید.

## تغییر نام مخزن

در GitHub به **Settings > General > Repository name** بروید و نام را به `computational-pathology-ai-lab` تغییر دهید.

## فعال‌سازی GitHub Pages

در **Settings > Pages**، قسمت Source را روی **GitHub Actions** قرار دهید. Workflow موجود در مخزن سایت را از پوشهٔ `website` منتشر می‌کند.

## انتشار نسخهٔ اول

پس از سبزشدن تست‌ها، Tag با نام `v1.0.0` بسازید و Release را منتشر کنید. برای نرم‌افزار یک DOI جداگانه از Zenodo بگیرید؛ DOI `10.5281/zenodo.21444837` متعلق به کتاب است.
