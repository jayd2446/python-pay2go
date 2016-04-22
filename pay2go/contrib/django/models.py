# coding: utf-8

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


# TODO
class Merchant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='merchants')
    member_unified = models.CharField(_('會員證號'), max_length=10, help_text=_('企業請提供統一編號；個人請提供身分證字號'))
    id_card_date = models.DateField(_('身份證發證日期'), null=True, blank=True, help_text=_('格式為：民國年 + 月 + 日，例：1040101'))
    id_card_place = models.CharField(_('身份證發證地點'), max_length=10, blank=True, default='', help_text=_('例：北市'))
    member_name = models.CharField(_('會員名稱'), max_length=20, help_text=_('企業請提供公司登記之名稱；個人請提供身分證登記姓名'))
    member_phone = models.CharField(_('會員電話'), max_length=13, help_text=_('可為市話或手機，例：02-000111 或 0912-000111'))
    manager_name = models.CharField(_('管理者姓名'), max_length=10)
    manager_name_e = models.CharField(_('管理者英文姓名'), max_length=20, help_text=_('格式為「名, 姓」，例：Xiao ming, Wang'))
    login_account = models.CharField(_('管理者帳號'), max_length=20, help_text=_('只接受英文、數字及 "_" "." "@" 三種符號'))
    manager_mobile = models.CharField(_('管理者行動電話號碼'), max_length=10, help_text=_('格式為 10 碼數字，例：0912000111'))
    manager_email = models.EmailField(_('管理者 Email'))
    merchant_id = models.CharField(_('商店代號'), max_length=15, help_text=_('格式為金流合作推廣商代號（3 碼，限大寫英文字）+ 自訂編號（最長 12 碼，限數字）'))
    merchant_name = models.CharField(_('商店中文名稱'), max_length=20)
    merchant_name_e = models.CharField(_('商店英文名稱'), max_length=100)
    merchant_web_url = models.URLField(_('商店網址'))
    merchant_addr_city = models.CharField(_('聯絡地址 - 城市'), max_length=5, help_text=_('例：新北市、台南市'))
    merchant_addr_area = models.CharField(_('聯絡地址 - 地區'), max_length=5, help_text=_('例：中區、新營區。'))
    merchant_addr_code = models.CharField(_('聯絡地址 - 郵遞區號'), max_length=3, help_text=_('例：台北市中正區，則帶 100'))
    merchant_addr = models.CharField(_('聯絡地址 - 路名及門牌號碼'), max_length=60)
    national_e = models.CharField(_('設立登記營業國家（英文名）'), max_length=60, help_text=_('例：Taiwan'))
    city_e = models.CharField(_('設立登記營業城市（英文名）'), max_length=60, help_text=_('例：Taipei City'))
    merchant_type = models.IntegerField(_('販售商品型態'), )
    business_type = models.CharField(_('商品類別'), max_length=4)
    merchant_desc = models.CharField(_('商店簡介'), max_length=255)
    bank_code = models.CharField(_('會員金融機構帳戶金融機構代碼'), max_length=3)
    bank_branch_code = models.CharField(_('會員金融機構帳戶金融機構分行代碼'), max_length=4)
    bank_account = models.CharField(_('會員金融機構帳戶帳號'), max_length=30)
    payment_type = models.CharField(_('啟用支付方式'), max_length=255, blank=True, default='')
    agreed_fee = models.CharField(_('交易手續費'), max_length=255, blank=True, default='')
    agreed_day = models.CharField(_('撥款天數'), max_length=255, blank=True, default='')
    merchant_hash_key = models.CharField(_('商店 HashKey'), max_length=30, blank=True, default='')
    merchant_hash_iv = models.CharField(_('商店 Hash IV'), max_length=30, blank=True, default='')
    created_at = models.DateTimeField(_('建立時間'), auto_now_add=True)
    last_modified_at = models.DateTimeField(_('修改時間'), auto_now=True)

    class Meta:
        verbose_name = _('合作商店')
        verbose_name_plural = _('合作商店')
