<?php
// Seed Data Structure for CreditBridge - Multi-Company / Multi-Client Database
$initial_database = [
    "defong" => [
        "id" => "defong",
        "name" => "Defong Enterprise Sdn Bhd",
        "tin" => "C12345678900",
        "ssm" => "198301004532 (112345-U)",
        "industry" => "Hardware distribution",
        "client_id" => "DF-998877",
        "client_secret" => "••••••••••••••••",
        "do_method" => "whatsapp",
        "clients" => [
            "chuan_luck" => [
                "id" => "chuan_luck",
                "name" => "Chuan Luck Construction",
                "relationship" => "8-year customer · avg 67 days",
                "health_status" => "Prime",
                "health_score" => 782,
                "frequency" => "High",
                "frequency_rate" => "3.2× / month",
                "payment_days" => 67,
                "promised_days" => 60,
                "coop_years" => 8,
                "trend" => "Growing",
                "total_transacted" => "RM 2.4M",
                "invoices" => [
                    [
                        "invoice_no" => "INV-2026-0441",
                        "amount" => 85000,
                        "date" => "2026-05-05",
                        "status" => "Overdue",
                        "overdue_days" => 23,
                        "einvoice" => "verified",
                        "bank" => "verified",
                        "do" => "pending",
                        "pdpa_signed" => false,
                        "pdpa_reference" => "CBR-PDPA-2026-0441",
                        "pdpa_requested_at" => "June 28, 2026 at 14:32",
                        "financing_status" => "none"
                    ],
                    [
                        "invoice_no" => "INV-2026-0390",
                        "amount" => 45000,
                        "date" => "2026-04-12",
                        "status" => "Paid",
                        "overdue_days" => 0,
                        "einvoice" => "verified",
                        "bank" => "verified",
                        "do" => "verified",
                        "pdpa_signed" => false,
                        "pdpa_reference" => "CBR-PDPA-2026-0390",
                        "pdpa_requested_at" => "April 12, 2026 at 09:15",
                        "financing_status" => "none"
                    ]
                ]
            ],
            "kl_premier" => [
                "id" => "kl_premier",
                "name" => "KL Premier Builders",
                "relationship" => "3-year customer · avg 55 days",
                "health_status" => "Amber",
                "health_score" => 550,
                "frequency" => "Medium",
                "frequency_rate" => "1.8× / month",
                "payment_days" => 78,
                "promised_days" => 60,
                "coop_years" => 3,
                "trend" => "Stable",
                "total_transacted" => "RM 850k",
                "invoices" => [
                    [
                        "invoice_no" => "INV-2026-0438",
                        "amount" => 142500,
                        "date" => "2026-06-20",
                        "status" => "Due Soon",
                        "overdue_days" => 8,
                        "einvoice" => "verified",
                        "bank" => "verified",
                        "do" => "verified",
                        "pdpa_signed" => false,
                        "pdpa_reference" => "CBR-PDPA-2026-0438",
                        "pdpa_requested_at" => "June 20, 2026 at 11:00",
                        "financing_status" => "none"
                    ]
                ]
            ],
            "sunrise" => [
                "id" => "sunrise",
                "name" => "Sunrise Contractors",
                "relationship" => "2-year customer · avg 45 days",
                "health_status" => "Toxic",
                "health_score" => 320,
                "frequency" => "Low",
                "frequency_rate" => "0.8× / month",
                "payment_days" => 110,
                "promised_days" => 60,
                "coop_years" => 2,
                "trend" => "Shrinking",
                "total_transacted" => "RM 310k",
                "invoices" => [
                    [
                        "invoice_no" => "INV-2026-0429",
                        "amount" => 67800,
                        "date" => "2026-06-01",
                        "status" => "Paid",
                        "overdue_days" => 0,
                        "einvoice" => "verified",
                        "bank" => "verified",
                        "do" => "verified",
                        "pdpa_signed" => false,
                        "pdpa_reference" => "CBR-PDPA-2026-0429",
                        "pdpa_requested_at" => "June 01, 2026 at 10:20",
                        "financing_status" => "none"
                    ],
                    [
                        "invoice_no" => "INV-2026-0415",
                        "amount" => 54000,
                        "date" => "2026-05-10",
                        "status" => "Overdue",
                        "overdue_days" => 18,
                        "einvoice" => "verified",
                        "bank" => "pending",
                        "do" => "pending",
                        "pdpa_signed" => false,
                        "pdpa_reference" => "CBR-PDPA-2026-0415",
                        "pdpa_requested_at" => "May 10, 2026 at 16:00",
                        "financing_status" => "none"
                    ]
                ]
            ]
        ]
    ],
    "apex" => [
        "id" => "apex",
        "name" => "Apex Distribution Sdn Bhd",
        "tin" => "C98765432100",
        "ssm" => "201001099887 (987654-A)",
        "industry" => "Logistics & Warehousing",
        "client_id" => "AP-112233",
        "client_secret" => "••••••••••••••••",
        "do_method" => "driver_app",
        "clients" => [
            "bina_raya" => [
                "id" => "bina_raya",
                "name" => "Bina Raya Builders",
                "relationship" => "4-year customer · avg 73 days",
                "health_status" => "Amber",
                "health_score" => 620,
                "frequency" => "Medium",
                "frequency_rate" => "2.1× / month",
                "payment_days" => 73,
                "promised_days" => 60,
                "coop_years" => 4,
                "trend" => "Stable",
                "total_transacted" => "RM 1.2M",
                "invoices" => [
                    [
                        "invoice_no" => "INV-2026-0881",
                        "amount" => 58000,
                        "date" => "2026-06-02",
                        "status" => "Overdue",
                        "overdue_days" => 10,
                        "einvoice" => "verified",
                        "bank" => "pending",
                        "do" => "verified",
                        "pdpa_signed" => false,
                        "pdpa_reference" => "CBR-PDPA-2026-0881",
                        "pdpa_requested_at" => "June 02, 2026 at 15:45",
                        "financing_status" => "none"
                    ],
                    [
                        "invoice_no" => "INV-2026-0840",
                        "amount" => 42000,
                        "date" => "2026-05-01",
                        "status" => "Paid",
                        "overdue_days" => 0,
                        "einvoice" => "verified",
                        "bank" => "verified",
                        "do" => "verified",
                        "pdpa_signed" => false,
                        "pdpa_reference" => "CBR-PDPA-2026-0840",
                        "pdpa_requested_at" => "May 01, 2026 at 09:30",
                        "financing_status" => "none"
                    ]
                ]
            ],
            "maju_jaya" => [
                "id" => "maju_jaya",
                "name" => "Maju Jaya Contractors",
                "relationship" => "1-year customer · avg 120 days",
                "health_status" => "Toxic",
                "health_score" => 410,
                "frequency" => "Low",
                "frequency_rate" => "0.5× / month",
                "payment_days" => 120,
                "promised_days" => 60,
                "coop_years" => 1,
                "trend" => "Shrinking",
                "total_transacted" => "RM 150k",
                "invoices" => [
                    [
                        "invoice_no" => "INV-2026-0901",
                        "amount" => 32000,
                        "date" => "2026-06-10",
                        "status" => "Due Soon",
                        "overdue_days" => 5,
                        "einvoice" => "pending",
                        "bank" => "pending",
                        "do" => "verified",
                        "pdpa_signed" => false,
                        "pdpa_reference" => "CBR-PDPA-2026-0901",
                        "pdpa_requested_at" => "June 10, 2026 at 10:15",
                        "financing_status" => "none"
                    ]
                ]
            ]
        ]
    ]
];

// Maintain compatibility for any script checking $contractors array directly
$contractors = [];
foreach ($initial_database as $comp) {
    foreach ($comp['clients'] as $cli_id => $cli) {
        $contractors[$cli_id] = [
            "id" => $cli_id,
            "name" => $cli['name'],
            "owe_amount" => number_format(array_sum(array_column(array_filter($cli['invoices'], function($i) { return $i['status'] !== 'Paid' && $i['financing_status'] !== 'Financed'; }), 'amount'))),
            "health_status" => $cli['health_status'],
            "health_score" => round($cli['health_score'] / 10),
            "frequency" => $cli['frequency'],
            "payment_days" => $cli['payment_days'],
            "coop_years" => $cli['coop_years'],
            "trend" => $cli['trend']
        ];
    }
}
?>
