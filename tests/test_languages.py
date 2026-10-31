from pathlib import Path
import json,shutil,subprocess,sys,tempfile,unittest

ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/'skills/deepseen-asset-quality-audit/scripts/check_media_review.py'

@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'),'ffmpeg and ffprobe required')
class ReviewLanguageTests(unittest.TestCase):
    def test_localized_receipts_preserve_technical_facts_and_unverified_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp=Path(tmp);media=tmp/'synthetic.mp4';review=tmp/'review.json';review.write_text('{}',encoding='utf-8')
            subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-f','lavfi','-i','color=c=blue:s=128x128:d=1','-an','-c:v','libx264',str(media)],check=True)
            results=[]
            for lang in ['zh-CN','en']:
                output=tmp/(lang+'.json')
                r=subprocess.run([sys.executable,'-I','-S','-X','utf8',str(SCRIPT),'--media',str(media),'--review',str(review),'--output',str(output),'--lang',lang],capture_output=True,encoding='utf-8')
                self.assertEqual(r.returncode,0,r.stderr)
                results.append(json.loads(output.read_text(encoding='utf-8')))
            self.assertEqual(results[0]['media'],results[1]['media'])
            self.assertEqual(results[0]['review']['status'],'unverified')
            self.assertEqual(results[1]['review']['status'],'unverified')
            self.assertIn('noticeEn',results[1]['review'])
            self.assertTrue(all('reasonEn' in row and 'reasonZh' not in row for row in results[1]['review']['checks']))

if __name__=='__main__':unittest.main()
