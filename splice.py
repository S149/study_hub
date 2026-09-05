# -*- coding: utf-8 -*-
with open('/home/claude/work/istqb-hub.html', encoding='utf-8') as f:
    content = f.read()

with open('/home/claude/work/ctal-ta/blocks/all_tocs.html', encoding='utf-8') as f:
    tocs = f.read().rstrip('\n')
with open('/home/claude/work/ctal-ta/blocks/all_hubitems.html', encoding='utf-8') as f:
    hubitems = f.read().rstrip('\n')
with open('/home/claude/work/ctal-ta/blocks/all_views.html', encoding='utf-8') as f:
    views = f.read().rstrip('\n')

# 1. Splice TOCCHAPTER blocks into sidebar nav, after the 6th toc-chapter's closing </div>, before </nav>
anchor_toc = '''      </div>
    </div>
  </nav>'''
assert content.count(anchor_toc) == 1, ("toc anchor count", content.count(anchor_toc))
divider_toc = '\n    <div class="toc-section-divider"><span>Advanced Level &middot; Test Analyst (CTAL-TA)</span></div>\n'
replacement_toc = '''      </div>
    </div>''' + divider_toc + tocs + '\n  </nav>'
content = content.replace(anchor_toc, replacement_toc, 1)

# 2. Splice HUBITEM blocks into hub list, after 6th hubitem's closing </li>, before </ul></section>
anchor_hub = '''      </li>
    </ul>
  </section>
</main>'''
assert content.count(anchor_hub) == 1, ("hub anchor count", content.count(anchor_hub))
divider_hub = '\n    </ul>\n    <div class="hublist-divider"><span>Advanced Level &middot; Test Analyst (CTAL-TA)</span></div>\n    <ul class="hublist">\n'
replacement_hub = '''      </li>''' + divider_hub + hubitems + '\n    </ul>\n  </section>\n</main>'
content = content.replace(anchor_hub, replacement_hub, 1)

# 3. Splice VIEW blocks into document body, right after view-ch6 closes (marked by the ch6 footer + closing divs)
anchor_view = '''  <span class="step">Chapter 6 of 6</span>
  <span class="step"></span>
</footer>


</div>

</div>
</div>
'''
assert content.count(anchor_view) == 1, ("view anchor count", content.count(anchor_view))
replacement_view = '''  <span class="step">Chapter 6 of 6</span>
  <span class="step"></span>
</footer>


</div>

''' + views + '''

</div>
</div>
'''
content = content.replace(anchor_view, replacement_view, 1)

with open('/home/claude/work/istqb-hub.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("all spliced ok")
