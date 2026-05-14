# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_10:39:38_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-05-14 10:39:38 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-14 10:39:38 UTC

- **81,462** saved flights
- **29,521** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **81,462** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,003,683.8 tonnes** estimated CO2 emissions
- **58,184,568 km** total distance flown
- **864 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3493 |
| 2 | SkyWest Airlines | 3020 |
| 3 | IndiGo | 1793 |
| 4 | EJA | 1525 |
| 5 | American Airlines | 1255 |
| 6 | Southwest Airlines | 1190 |
| 7 | Lufthansa | 1058 |
| 8 | ENY | 1019 |
| 9 | Delta Air Lines | 894 |
| 10 | Vueling | 774 |
| 11 | AXM | 744 |
| 12 | LATAM Airlines | 741 |
| 13 | WIF | 706 |
| 14 | All Nippon Airways | 646 |
| 15 | AZU | 640 |
| 16 | Swiss International | 637 |
| 17 | QLK | 608 |
| 18 | LXJ | 592 |
| 19 | Alaska Airlines | 578 |
| 20 | easyJet | 542 |
| 21 | EJU | 525 |
| 22 | AEE | 520 |
| 23 | Cathay Pacific | 510 |
| 24 | VIV | 483 |
| 25 | Air France | 481 |
| 26 | Japan Airlines | 464 |
| 27 | AXB | 440 |
| 28 | CXK | 423 |
| 29 | AIQ | 406 |
| 30 | United Airlines | 403 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 66316 |
| 2 | 🇪🇸 ES | 5790 |
| 3 | 🇮🇳 IN | 5596 |
| 4 | 🇦🇺 AU | 5260 |
| 5 | 🇩🇪 DE | 4580 |
| 6 | 🇮🇹 IT | 4507 |
| 7 | 🇧🇷 BR | 4488 |
| 8 | 🇯🇵 JP | 4167 |
| 9 | 🇨🇦 CA | 4053 |
| 10 | 🇬🇧 GB | 3488 |
| 11 | 🇫🇷 FR | 3244 |
| 12 | 🇨🇴 CO | 2721 |
| 13 | 🇲🇽 MX | 2454 |
| 14 | 🇬🇷 GR | 2375 |
| 15 | 🇳🇴 NO | 2274 |
| 16 | 🇨🇭 CH | 2192 |
| 17 | 🇲🇾 MY | 1868 |
| 18 | 🇿🇦 ZA | 1538 |
| 19 | 🇹🇷 TR | 1449 |
| 20 | 🇳🇿 NZ | 1440 |
| 21 | 🇹🇭 TH | 1433 |
| 22 | 🇵🇱 PL | 1357 |
| 23 | 🇵🇭 PH | 1299 |
| 24 | 🇰🇷 KR | 1247 |
| 25 | 🇬🇹 GT | 1244 |
| 26 | 🇲🇦 MA | 951 |
| 27 | 🇲🇴 MO | 935 |
| 28 | 🇲🇪 ME | 874 |
| 29 | 🇳🇱 NL | 842 |
| 30 | 🇭🇷 HR | 722 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1785 |
| 2 | Tokyo International Airport |  | JP | 1396 |
| 3 | Denver International Airport |  | US | 1367 |
| 4 | Indira Gandhi International Airport |  | IN | 1185 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1163 |
| 6 | Frankfurt am Main International Airport |  | DE | 1069 |
| 7 | Harry Reid International Airport |  | US | 1011 |
| 8 | Zurich Airport |  | CH | 974 |
| 9 | La Aurora Airport |  | GT | 939 |
| 10 | Macau International Airport |  | MO | 935 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 919 |
| 12 | Guaymaral Airport |  | CO | 913 |
| 13 | El Dorado International Airport |  | CO | 879 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 823 |
| 15 | Chicago O'Hare International Airport |  | US | 791 |
| 16 | Madrid Barajas International Airport |  | ES | 745 |
| 17 | Kuala Lumpur International Airport |  | MY | 745 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 711 |
| 19 | Malpensa International Airport |  | IT | 690 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 689 |
| 21 | Bengaluru International Airport |  | IN | 688 |
| 22 | Salt Lake City International Airport |  | US | 673 |
| 23 | Capua Airport |  | IT | 665 |
| 24 | Charles de Gaulle International Airport |  | FR | 639 |
| 25 | Charlotte/Douglas International Airport |  | US | 634 |
| 26 | Congonhas Airport |  | BR | 633 |
| 27 | Tenerife Norte Airport |  | ES | 599 |
| 28 | Ninoy Aquino International Airport |  | PH | 594 |
| 29 | Daniel K Inouye International Airport |  | US | 590 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 586 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 545 |
| 32 | Barcelona International Airport |  | ES | 545 |
| 33 | Atizapan De Zaragoza Airport |  | MX | 542 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 527 |
| 35 | Don Mueang International Airport |  | TH | 516 |
| 36 | Vitoria/Foronda Airport |  | ES | 513 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 510 |
| 38 | Amsterdam Airport Schiphol |  | NL | 507 |
| 39 | O. R. Tambo International Airport |  | ZA | 488 |
| 40 | Calgary International Airport |  | CA | 480 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 380 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 294 | 21m | 244 km | 1,238.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 236 | 24m | 225 km | 915.6 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 219 | 28m | 304 km | 1,148.1 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 219 | 1h 27m | 910 km | 3,436.6 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 210 | 14m | 114 km | 411.9 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 208 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 194 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 187 | 19m | 165 km | 531.9 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 185 | 1h 11m | 770 km | 2,457.6 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 170 | 26m | 275 km | 805.6 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 142 | 20m | 99 km | 243.2 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 137 | 44m | 452 km | 1,067.7 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 128 | 31m | 369 km | 814.8 t |
| 16 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 121 | 27m | 215 km | 448.1 t |
| 17 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 120 | 27m | 152 km | 313.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 118 | 20m | 147 km | 298.6 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 117 | 14m | 154 km | 310.0 t |
| 20 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 116 | 20m | 250 km | 501.1 t |
| 21 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 22 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 23 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 109 | 1h 2m | 695 km | 1,306.6 t |
| 24 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 109 | 23m | 55 km | 103.6 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 106 | 1h 42m | 1,423 km | 2,601.4 t |
| 26 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 103 | 18m | 144 km | 256.2 t |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 102 | 12m | - | - |
| 29 | Bodø Airport (ENBO) | ENEN (ENEN) | 101 | 13m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 99 | 1h 41m | 1,156 km | 1,975.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| PLF130 | PLF | Szczecin-Goleniow Solidarność Airport (EPSC) | Rzeszow-Jasionka Airport (EPRZ) | 2026-05-14 09:39 UTC | 2026-05-14 10:39 UTC | 59m |
| N490LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-05-14 08:08 UTC | 2026-05-14 10:33 UTC | 2h 25m |
| N472LP |  | Glendale Regional Airport (KGEU) | Glendale Regional Airport (KGEU) | 2026-05-14 08:16 UTC | 2026-05-14 10:31 UTC | 2h 15m |
| CPA831 | Cathay Pacific | John F Kennedy International Airport (KJFK) | Macau International Airport (VMMC) | 2026-05-13 19:24 UTC | 2026-05-14 10:27 UTC | 15h 3m |
| IOS224 | IOS | St. Mary's Airport (EGHE) | Newquay Cornwall Airport (EGHQ) | 2026-05-14 10:02 UTC | 2026-05-14 10:26 UTC | 24m |
| NIJ | NIJ | Colac Airport (YOLA) | Melbourne Moorabbin Airport (YMMB) | 2026-05-14 09:00 UTC | 2026-05-14 10:20 UTC | 1h 20m |
| PHAFW | PHA | Texel Airport (EHTX) | Texel Airport (EHTX) | 2026-05-14 09:43 UTC | 2026-05-14 10:20 UTC | 36m |
| AE976 |  | Sydney Bankstown Airport (YSBK) | Orange Airport (YORG) | 2026-05-14 09:54 UTC | 2026-05-14 10:18 UTC | 23m |
| ZUIFY | ZUI | Delta 200 Airstrip (FADX) | Delta 200 Airstrip (FADX) | 2026-05-14 10:12 UTC | 2026-05-14 10:13 UTC | 1m |
| SWR5EC | Swiss International | Bordeaux-Merignac (BA 106) Airport (LFBD) | Zurich Airport (LSZH) | 2026-05-14 09:01 UTC | 2026-05-14 10:10 UTC | 1h 9m |
| RP1251 |  | Ninoy Aquino International Airport (RPLL) | Loakan Airport (RPUB) | 2026-05-14 09:48 UTC | 2026-05-14 10:09 UTC | 21m |
| PHJVZ | PHJ | Seppe Airport (EHSE) | Rotterdam Airport (EHRD) | 2026-05-14 09:26 UTC | 2026-05-14 10:08 UTC | 41m |
| FIN9VM | Finnair | Helsinki Vantaa Airport (EFHK) | Vaasa Airport (EFVA) | 2026-05-14 09:26 UTC | 2026-05-14 10:07 UTC | 40m |
| OKHKI | OKH | Hradec Kralove Airport (LKHK) | Hradec Kralove Airport (LKHK) | 2026-05-14 10:01 UTC | 2026-05-14 10:01 UTC | 0m |
| VLG9FT | Vueling | Palma De Mallorca Airport (LEPA) | Federico Garcia Lorca Airport (LEGR) | 2026-05-14 08:55 UTC | 2026-05-14 10:00 UTC | 1h 5m |
| COL360 | COL | Shannon Airport (EINN) | Bristol International Airport (EGGD) | 2026-05-14 09:14 UTC | 2026-05-14 09:59 UTC | 44m |
| OKVIP | OKV | Graz Airport (LOWG) | Otocac Airport (LDRO) | 2026-05-14 09:13 UTC | 2026-05-14 09:57 UTC | 44m |
| AIQ3207 | AIQ | Don Mueang International Airport (VTBD) | Kengtung Airport (VYKG) | 2026-05-14 09:06 UTC | 2026-05-14 09:57 UTC | 50m |
| BHA557 | BHA | Tribhuvan International Airport (VNKT) | Tribhuvan International Airport (VNKT) | 2026-05-14 09:51 UTC | 2026-05-14 09:56 UTC | 5m |
| RYR7209 | Ryanair | Valencia Airport (LEVC) | Ibiza Airport (LEIB) | 2026-05-14 09:21 UTC | 2026-05-14 09:51 UTC | 30m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
